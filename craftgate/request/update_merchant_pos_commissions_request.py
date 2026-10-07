from typing import List, Optional

from craftgate.request.common.base_request import BaseRequest
from craftgate.request.dto.update_merchant_pos_commission import UpdateMerchantPosCommission


class UpdateMerchantPosCommissionsRequest(BaseRequest):
    def __init__(self, commissions: Optional[List[UpdateMerchantPosCommission]] = None) -> None:
        self.commissions = commissions
