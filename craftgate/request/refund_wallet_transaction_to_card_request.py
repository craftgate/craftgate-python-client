from decimal import Decimal


class RefundWalletTransactionToCardRequest(object):
    def __init__(self, refund_price=None):
        # type: (Decimal) -> None
        self.refund_price = refund_price
