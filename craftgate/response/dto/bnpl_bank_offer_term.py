from decimal import Decimal
from typing import Optional


class BnplBankOfferTerm(object):
    def __init__(
            self,
            term: Optional[int] = None,
            amount: Optional[Decimal] = None,
            total_amount: Optional[Decimal] = None,
            interest_rate: Optional[Decimal] = None,
            annual_interest_rate: Optional[Decimal] = None
    ) -> None:
        self.term = term
        self.amount = amount
        self.total_amount = total_amount
        self.interest_rate = interest_rate
        self.annual_interest_rate = annual_interest_rate
