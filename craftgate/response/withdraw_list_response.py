from craftgate.response.common.list_response import ListResponse
from craftgate.response.withdraw_response import WithdrawResponse


class WithdrawListResponse(ListResponse[WithdrawResponse]):
    item_type = WithdrawResponse
