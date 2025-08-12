from decimal import Decimal
from craftgate.model.currency import Currency


class CreateWalletRequest(object):
    def __init__(self, negative_amount_limit=None, currency=None):
        # type: (Decimal, Currency) -> None
        self.negative_amount_limit = negative_amount_limit
        self.currency = currency
