from typing import Any, Generic, Iterable, List, Mapping, Optional, Type, TypeVar, cast

from craftgate.utils.attribute_dict import AttributeDict
from craftgate.utils.converter import Converter

TItem = TypeVar("TItem")
ListResponseType = TypeVar("ListResponseType", bound="ListResponse[Any]")


class ListResponse(Generic[TItem]):
    item_type: Optional[Type[Any]] = None

    def __init__(
            self,
            items: Optional[Iterable[TItem]] = None,
            page: Optional[int] = None,
            size: Optional[int] = None,
            total_size: Optional[int] = None
    ):
        self.items: List[TItem] = self._map_items(items or [])
        self.page = page
        self.size = size
        self.total_size = total_size

    @classmethod
    def from_dict(cls: Type[ListResponseType], data: Optional[Mapping[str, Any]]) -> ListResponseType:
        payload = data or {}
        items = payload.get("items", [])
        return cls(
            items=[cls._coerce_item(item) for item in items],
            page=payload.get("page"),
            size=payload.get("size"),
            total_size=payload.get("totalSize")
        )

    @classmethod
    def _coerce_item(cls, item: Any) -> TItem:
        target_type = cls.item_type
        if target_type and isinstance(item, dict):
            return cast(TItem, Converter.auto_map(target_type, item))
        if target_type:
            return cast(TItem, Converter.coerce_value(item, target_type))
        if isinstance(item, dict):
            return cast(TItem, AttributeDict(item))
        return cast(TItem, item)

    def _map_items(self, items: Iterable[Any]) -> List[TItem]:
        return [self._coerce_item(item) for item in items]

    def to_dict(self):
        return {
            "items": [Converter.to_clean_dict(item) for item in self.items],
            "page": self.page,
            "size": self.size,
            "totalSize": self.total_size
        }

    def __repr__(self):
        return "ListResponse(items=%r, page=%r, size=%r, total_size=%r)" % (
            self.items, self.page, self.size, self.total_size)
