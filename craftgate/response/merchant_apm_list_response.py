from craftgate.response.common.list_response import ListResponse
from craftgate.response.merchant_apm_response import MerchantApmResponse


class MerchantApmListResponse(ListResponse[MerchantApmResponse]):
    item_type = MerchantApmResponse
