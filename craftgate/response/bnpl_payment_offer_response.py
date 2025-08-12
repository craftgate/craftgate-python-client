from typing import Optional, List
from decimal import Decimal
from craftgate.response.dto.bnpl_bank_offer import BnplBankOffer

class BnplPaymentOfferResponse(object):
    def __init__(
        self,
        offer_id=None,               # type: Optional[str]
        price=None,                   # type: Optional[Decimal]
        bank_offers=None              # type: Optional[List[BnplBankOffer]]
    ):
        self.offer_id = offer_id
        self.price = price
        self.bank_offers = bank_offers