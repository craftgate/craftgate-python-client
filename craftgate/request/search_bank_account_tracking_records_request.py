from datetime import datetime
from typing import Optional

from craftgate.model.currency import Currency


class SearchBankAccountTrackingRecordsRequest:
    def __init__(
        self,
        currency: Optional[Currency] = None,
        description: Optional[str] = None,
        sender_name: Optional[str] = None,
        sender_iban: Optional[str] = None,
        min_record_date: Optional[datetime] = None,
        max_record_date: Optional[datetime] = None,
        page: int = 0,
        size: int = 10
    ) -> None:
        self.currency = currency
        self.description = description
        self.sender_name = sender_name
        self.sender_iban = sender_iban
        self.min_record_date = min_record_date
        self.max_record_date = max_record_date
        self.page = page
        self.size = size
