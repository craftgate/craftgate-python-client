import re
from typing import Any, Iterable, Mapping, Optional, Tuple


class AttributeDict(dict):
    __slots__ = ("_attr_to_key",)

    _first_cap_pattern = re.compile(r"(.)([A-Z][a-z]+)")
    _camel_pattern = re.compile(r"([a-z0-9])([A-Z])")
    _sentinel = object()

    def __init__(self, initial: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> None:
        object.__setattr__(self, "_attr_to_key", {})
        super().__init__()
        if initial:
            prepared = initial if isinstance(initial, Mapping) else dict(initial)
            self._update_from_mapping(prepared)
        if kwargs:
            self._update_from_mapping(kwargs)

    def __setitem__(self, key: str, value: Any) -> None:
        wrapped = self._wrap(value)
        super().__setitem__(key, wrapped)
        if isinstance(key, str):
            attr_name = self._normalize_key(key)
            self._attr_to_key[attr_name] = key

    def __delitem__(self, key: str) -> None:
        super().__delitem__(key)
        if isinstance(key, str):
            attr_name = self._normalize_key(key)
            self._attr_to_key.pop(attr_name, None)

    def update(self, *args: Any, **kwargs: Any) -> None:
        for mapping in args:
            for key, value in self._iterate_items(mapping):
                self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def pop(self, key: str, default: Any = _sentinel):
        if isinstance(key, str) and key in self:
            attr_name = self._normalize_key(key)
            self._attr_to_key.pop(attr_name, None)
        if default is self._sentinel:
            return super().pop(key)
        return super().pop(key, default)

    def popitem(self):
        key, value = super().popitem()
        if isinstance(key, str):
            attr_name = self._normalize_key(key)
            self._attr_to_key.pop(attr_name, None)
        return key, value

    def clear(self) -> None:
        super().clear()
        self._attr_to_key.clear()

    def setdefault(self, key: str, default: Any = None):
        if key not in self:
            self[key] = default
        return self[key]

    def copy(self):
        return AttributeDict(self)

    def __getattr__(self, item: str) -> Any:
        attr_map = object.__getattribute__(self, "_attr_to_key")
        if item in attr_map:
            return self[attr_map[item]]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'.")

    def __setattr__(self, key: str, value: Any) -> None:
        if key in self.__class__.__dict__ or key.startswith("_"):
            object.__setattr__(self, key, value)
            return
        attr_map = object.__getattribute__(self, "_attr_to_key")
        if key in attr_map:
            original_key = attr_map[key]
        else:
            original_key = key
        self[original_key] = value

    def __delattr__(self, item: str) -> None:
        if item.startswith("_") or item in self.__class__.__dict__:
            object.__delattr__(self, item)
            return
        attr_map = object.__getattribute__(self, "_attr_to_key")
        if item in attr_map:
            del self[attr_map[item]]
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'.")

    def __dir__(self) -> Iterable[str]:
        base_dir = super().__dir__()
        attr_map = object.__getattribute__(self, "_attr_to_key")
        return list(base_dir) + list(attr_map.keys())

    def to_dict(self) -> Mapping[str, Any]:
        return {key: self._unwrap(value) for key, value in self.items()}

    @classmethod
    def _wrap(cls, value: Any) -> Any:
        if isinstance(value, AttributeDict):
            return value
        if isinstance(value, Mapping):
            return cls(value)
        if isinstance(value, list):
            return [cls._wrap(v) for v in value]
        return value

    @classmethod
    def _unwrap(cls, value: Any) -> Any:
        if isinstance(value, AttributeDict):
            return value.to_dict()
        if isinstance(value, list):
            return [cls._unwrap(v) for v in value]
        return value

    def _update_from_mapping(self, mapping: Mapping[str, Any]) -> None:
        for key, value in mapping.items():
            self[key] = value

    @staticmethod
    def _iterate_items(mapping: Any) -> Iterable[Tuple[Any, Any]]:
        if isinstance(mapping, Mapping):
            return mapping.items()
        return dict(mapping).items()

    @classmethod
    def _normalize_key(cls, key: str) -> str:
        s1 = cls._first_cap_pattern.sub(r"\1_\2", key)
        return cls._camel_pattern.sub(r"\1_\2", s1).lower()

    def __repr__(self) -> str:
        return f"AttributeDict({dict(self)!r})"
