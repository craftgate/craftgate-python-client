from craftgate.response.common.list_response import ListResponse
from craftgate.response.member_response import MemberResponse


class MemberListResponse(ListResponse[MemberResponse]):
    item_type = MemberResponse
