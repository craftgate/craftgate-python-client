from decimal import Decimal
from typing import List, Optional

from craftgate.response.dto.bnpl_bank_offer import BnplBankOffer


class BnplPaymentOfferResponse(object):
    def __init__(
            self,
            offer_id: Optional[str] = None,
            price: Optional[Decimal] = None,
            bank_offers: Optional[List[BnplBankOffer]] = None
    ) -> None:
        self.offer_id = offer_id
        self.price = price
        self.bank_offers = bank_offers
