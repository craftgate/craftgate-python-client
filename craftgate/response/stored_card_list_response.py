from craftgate.response.common.list_response import ListResponse
from craftgate.response.stored_card_response import StoredCardResponse


class StoredCardListResponse(ListResponse[StoredCardResponse]):
    item_type = StoredCardResponse
