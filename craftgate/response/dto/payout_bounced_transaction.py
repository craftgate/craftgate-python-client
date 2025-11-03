from datetime import datetime
from decimal import Decimal
from typing import Optional


class PayoutBouncedTransaction(object):
    def __init__(
            self,
            id: Optional[int] = None,
            iban: Optional[str] = None,
            created_date: Optional[datetime] = None,
            updated_date: Optional[datetime] = None,
            payout_id: Optional[int] = None,
            payout_amount: Optional[Decimal] = None,
            contact_name: Optional[str] = None,
            contact_surname: Optional[str] = None,
            legal_company_title: Optional[str] = None,
            row_description: Optional[str] = None
    ) -> None:
        self.id = id
        self.iban = iban
        self.created_date = created_date
        self.updated_date = updated_date
        self.payout_id = payout_id
        self.payout_amount = payout_amount
        self.contact_name = contact_name
        self.contact_surname = contact_surname
        self.legal_company_title = legal_company_title
        self.row_description = row_description
