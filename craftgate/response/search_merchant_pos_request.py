from typing import Optional, List

from craftgate.response.merchant_pos_response import MerchantPosResponse


class MerchantPosListResponse(object):
    def __init__(self, items=None):  # type: Optional[List[MerchantPosResponse]]
        self.items = items