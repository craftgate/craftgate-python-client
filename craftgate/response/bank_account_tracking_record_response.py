from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.bank_account_tracking_source import BankAccountTrackingSource
from craftgate.model.currency import Currency
from craftgate.model.record_type import RecordType


class BankAccountTrackingRecordResponse:
    def __init__(
            self,
            id: Optional[int] = None,
            key: Optional[str] = None,
            currency: Optional[Currency] = None,
            record_type: Optional[RecordType] = None,
            sender_name: Optional[str] = None,
            sender_iban: Optional[str] = None,
            description: Optional[str] = None,
            record_date: Optional[datetime] = None,
            amount: Optional[Decimal] = None,
            bank_account_tracking_source: Optional[BankAccountTrackingSource] = None
    ) -> None:
        self.id = id
        self.key = key
        self.currency = currency
        self.record_type = record_type
        self.sender_name = sender_name
        self.sender_iban = sender_iban
        self.description = description
        self.record_date = record_date
        self.amount = amount
        self.bank_account_tracking_source = bank_account_tracking_source
