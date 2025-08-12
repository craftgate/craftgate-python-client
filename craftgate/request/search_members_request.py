from typing import Optional, Set

from craftgate.model.member_type import MemberType


class SearchMembersRequest(object):
    def __init__(
            self,
            page: int = 0,
            size: int = 10,
            is_buyer: Optional[bool] = None,
            is_sub_merchant: Optional[bool] = None,
            name: Optional[str] = None,
            member_ids: Optional[Set[int]] = None,
            member_type: Optional[MemberType] = None,
            member_external_id: Optional[str] = None
    ) -> None:
        self.page = page
        self.size = size
        self.is_buyer = is_buyer
        self.is_sub_merchant = is_sub_merchant
        self.name = name
        self.member_ids = member_ids
        self.member_type = member_type
        self.member_external_id = member_external_id
