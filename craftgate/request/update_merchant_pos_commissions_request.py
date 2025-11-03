from typing import List, Optional

from craftgate.request.dto.update_merchant_pos_commission import UpdateMerchantPosCommission


class UpdateMerchantPosCommissionsRequest(object):
    def __init__(self, commissions: Optional[List[UpdateMerchantPosCommission]] = None) -> None:
        self.commissions = commissions
