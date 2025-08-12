from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.model.remittance_reason_type import RemittanceReasonType


class CreateRemittanceRequest(object):
    def __init__(
            self,
            member_id: Optional[int] = None,
            price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            description: Optional[str] = None,
            remittance_reason_type: Optional[RemittanceReasonType] = None
    ) -> None:
        self.member_id = member_id
        self.price = price
        self.currency = currency
        self.description = description
        self.remittance_reason_type = remittance_reason_type
