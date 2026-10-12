from decimal import Decimal
from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class ResetMerchantMemberWalletBalanceRequest(BaseRequest):
    def __init__(self, wallet_amount: Optional[Decimal] = None) -> None:
        self.wallet_amount = wallet_amount
