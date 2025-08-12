from craftgate.response.common.list_response import ListResponse
from craftgate.response.merchant_pos_commission_response import MerchantPosCommissionResponse


class MerchantPosCommissionListResponse(ListResponse[MerchantPosCommissionResponse]):
    item_type = MerchantPosCommissionResponse
