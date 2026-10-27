from craftgate.response.common.list_response import ListResponse
from craftgate.response.dto.payout_completed_item import PayoutCompletedItem


class PayoutCompletedItemListResponse(ListResponse[PayoutCompletedItem]):
    item_type = PayoutCompletedItem
