from typing import Optional
from decimal import Decimal

class BnplBankOfferTerm(object):
    def __init__(
        self,
        term=None,                   # type: Optional[int]
        amount=None,                  # type: Optional[Decimal]
        total_amount=None,            # type: Optional[Decimal]
        interest_rate=None,           # type: Optional[Decimal]
        annual_interest_rate=None     # type: Optional[Decimal]
    ):
        self.term = term
        self.amount = amount
        self.total_amount = total_amount
        self.interest_rate = interest_rate
        self.annual_interest_rate = annual_interest_rate