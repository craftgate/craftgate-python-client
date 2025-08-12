from typing import Optional
from datetime import datetime


class PayoutBouncedTransaction(object):
    def __init__(
        self,
        id=None,                     # type: Optional[int]
        iban=None,                   # type: Optional[str]
        created_date=None,           # type: Optional[datetime]
        updated_date=None,           # type: Optional[datetime]
        payout_id=None,              # type: Optional[int]
        payout_amount=None,          # type: Optional[float]
        contact_name=None,           # type: Optional[str]
        contact_surname=None,        # type: Optional[str]
        legal_company_title=None,    # type: Optional[str]
        row_description=None         # type: Optional[str]
    ):
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
