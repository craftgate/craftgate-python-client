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
        id=None,  # type: Optional[int]
        created_date=None,  # type: Optional[datetime]
        status=None,  # type: Optional[Status]
        price=None,  # type: Optional[Decimal]
        currency=None,  # type: Optional[Currency]
        member_id=None,  # type: Optional[int]
        remittance_type=None,  # type: Optional[RemittanceType]
        remittance_reason_type=None,  # type: Optional[RemittanceReasonType]
        description=None  # type: Optional[str]
    ):
        # type: (...) -> None
        self.id = id
        self.created_date = created_date
        self.status = status
        self.price = price
        self.currency = currency
        self.member_id = member_id
        self.remittance_type = remittance_type
        self.remittance_reason_type = remittance_reason_type
        self.description = description
