from craftgate.response.common.list_response import ListResponse
from craftgate.response.dto.payout_row import PayoutRow


class PayoutRowListResponse(ListResponse[PayoutRow]):
    item_type = PayoutRow
