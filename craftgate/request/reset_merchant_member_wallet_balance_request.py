from decimal import Decimal
from typing import Optional


class ResetMerchantMemberWalletBalanceRequest(object):
    def __init__(self, wallet_amount: Optional[Decimal] = None) -> None:
        self.wallet_amount = wallet_amount
