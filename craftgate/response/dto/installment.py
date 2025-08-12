from typing import Optional, List

from craftgate.model.card_type import CardType
from craftgate.model.card_association import CardAssociation
from craftgate.response.dto.installment_price import InstallmentPrice


class Installment(object):
    def __init__(
        self,
        bin_number=None,                     # type: Optional[str]
        price=None,                          # type: Optional[float]
        card_type=None,                      # type: Optional[CardType]
        card_association=None,               # type: Optional[CardAssociation]
        card_brand=None,                     # type: Optional[str]
        bank_name=None,                      # type: Optional[str]
        bank_code=None,                      # type: Optional[int]
        force3ds=None,                       # type: Optional[bool]
        cvc_required=None,                   # type: Optional[bool]
        commercial=None,                     # type: Optional[bool]
        installment_prices=None              # type: Optional[List[InstallmentPrice]]
    ):
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