from decimal import Decimal
from craftgate.model.currency import Currency


class CreateWithdrawRequest(object):
    def __init__(self, price=None, member_id=None, description=None, currency=None):
        # type: (Decimal, int, str, Currency) -> None
        self.price = price
        self.member_id = member_id
        self.description = description
        self.currency = currency
