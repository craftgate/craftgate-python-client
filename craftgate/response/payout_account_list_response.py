from craftgate.response.common.list_response import ListResponse
from craftgate.response.payout_account_response import PayoutAccountResponse


class PayoutAccountListResponse(ListResponse[PayoutAccountResponse]):
    item_type = PayoutAccountResponse
