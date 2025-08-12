from typing import List, Optional
from craftgate.response.merchant_apm_response import MerchantApmResponse

class MerchantApmListResponse(object):
    def __init__(self, items=None):
        # type: (Optional[List[MerchantApmResponse]]) -> None
        self.items = items