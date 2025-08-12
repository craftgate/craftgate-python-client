from typing import Optional, Set
from craftgate.model.member_type import MemberType


class SearchMembersRequest(object):
    def __init__(
        self,
        page=0,  # type: int
        size=10,  # type: int
        is_buyer=None,  # type: Optional[bool]
        is_sub_merchant=None,  # type: Optional[bool]
        name=None,  # type: Optional[str]
        member_ids=None,  # type: Optional[Set[int]]
        member_type=None,  # type: Optional[MemberType]
        member_external_id=None  # type: Optional[str]
    ):
        self.page = page
        self.size = size
        self.is_buyer = is_buyer
        self.is_sub_merchant = is_sub_merchant
        self.name = name
        self.member_ids = member_ids
        self.member_type = member_type
        self.member_external_id = member_external_id