from craftgate.response.common.list_response import ListResponse
from craftgate.response.merchant_pos_response import MerchantPosResponse


class MerchantPosListResponse(ListResponse[MerchantPosResponse]):
    item_type = MerchantPosResponse
