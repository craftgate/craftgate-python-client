from typing import Optional

from craftgate.model.card_type import CardType
from craftgate.model.card_association import CardAssociation


class BinNumberResponse(object):
    def __init__(
        self,
        bin_number=None,                  # type: Optional[str]
        card_type=None,                   # type: Optional[CardType]
        card_association=None,            # type: Optional[CardAssociation]
        card_brand=None,                  # type: Optional[str]
        bank_name=None,                   # type: Optional[str]
        bank_code=None,                   # type: Optional[int]
        commercial=None                   # type: Optional[bool]
    ):
        self.bin_number = bin_number
        self.card_type = card_type
        self.card_association = card_association
        self.card_brand = card_brand
        self.bank_name = bank_name
        self.bank_code = bank_code
        self.commercial = commercial