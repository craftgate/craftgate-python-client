from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.model.remittance_reason_type import RemittanceReasonType
from craftgate.model.remittance_type import RemittanceType
from craftgate.model.status import Status


class RemittanceResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            created_date: Optional[datetime] = None,
            status: Optional[Status] = None,
            price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            member_id: Optional[int] = None,
            remittance_type: Optional[RemittanceType] = None,
            remittance_reason_type: Optional[RemittanceReasonType] = None,
            description: Optional[str] = None
    ) -> None:
        self.id = id
        self.created_date = created_date
        self.status = status
        self.price = price
        self.currency = currency
        self.member_id = member_id
        self.remittance_type = remittance_type
        self.remittance_reason_type = remittance_reason_type
        self.description = description
