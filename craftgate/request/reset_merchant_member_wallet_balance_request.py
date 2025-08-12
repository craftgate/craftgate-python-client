from decimal import Decimal


class ResetMerchantMemberWalletBalanceRequest(object):
    def __init__(self, wallet_amount=None):
        # type: (Decimal) -> None
        self.wallet_amount = wallet_amount
