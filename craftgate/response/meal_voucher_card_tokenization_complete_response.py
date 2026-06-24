from typing import Optional
from decimal import Decimal


class MealVoucherCardTokenizationCompleteResponse:
    def __init__(
        self,
        session_id: Optional[str] = None,
        masked_card_number: Optional[str] = None,
        fingerprint: Optional[str] = None,
        balance: Optional[Decimal] = None
    ) -> None:
        self.session_id = session_id
        self.masked_card_number = masked_card_number
        self.fingerprint = fingerprint
        self.balance = balance
