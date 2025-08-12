from typing import Optional

from craftgate.model.card_type import CardType
from craftgate.model.card_association import CardAssociation


class BinNumberResponse(object):
    def __init__(
            self,
            bin_number: Optional[str] = None,
            card_type: Optional[CardType] = None,
            card_association: Optional[CardAssociation] = None,
            card_brand: Optional[str] = None,
            bank_name: Optional[str] = None,
            bank_code: Optional[int] = None,
            commercial: Optional[bool] = None
    ) -> None:
        self.bin_number = bin_number
        self.card_type = card_type
        self.card_association = card_association
        self.card_brand = card_brand
        self.bank_name = bank_name
        self.bank_code = bank_code
        self.commercial = commercial
