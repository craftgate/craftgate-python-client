from decimal import Decimal
from typing import List, Optional

from craftgate.model.card_association import CardAssociation
from craftgate.model.card_type import CardType
from craftgate.response.dto.installment_price import InstallmentPrice


class Installment(object):
    def __init__(
            self,
            bin_number: Optional[str] = None,
            price: Optional[Decimal] = None,
            card_type: Optional[CardType] = None,
            card_association: Optional[CardAssociation] = None,
            card_brand: Optional[str] = None,
            bank_name: Optional[str] = None,
            bank_code: Optional[int] = None,
            force3ds: Optional[bool] = None,
            cvc_required: Optional[bool] = None,
            commercial: Optional[bool] = None,
            installment_prices: Optional[List[InstallmentPrice]] = None
    ) -> None:
        self.bin_number = bin_number
        self.price = price
        self.card_type = card_type
        self.card_association = card_association
        self.card_brand = card_brand
        self.bank_name = bank_name
        self.bank_code = bank_code
        self.force3ds = force3ds
        self.cvc_required = cvc_required
        self.commercial = commercial
        self.installment_prices = installment_prices
