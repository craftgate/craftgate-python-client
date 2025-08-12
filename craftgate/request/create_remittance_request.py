from decimal import Decimal
from craftgate.model.currency import Currency
from craftgate.model.remittance_reason_type import RemittanceReasonType


class CreateRemittanceRequest(object):
    def __init__(self, member_id=None, price=None, currency=None, description=None, remittance_reason_type=None):
        # type: (int, Decimal, Currency, str, RemittanceReasonType) -> None
        self.member_id = member_id
        self.price = price
        self.currency = currency
        self.description = description
        self.remittance_reason_type = remittance_reason_type
