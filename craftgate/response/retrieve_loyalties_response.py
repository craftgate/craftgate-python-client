from typing import Optional, List

from craftgate.response.dto.merchant_pos import MerchantPos
from craftgate.model.loyalty import Loyalty


class RetrieveLoyaltiesResponse(object):
    def __init__(
        self,
        card_brand=None,                 # type: Optional[str]
        card_issuer_bank_name=None,     # type: Optional[str]
        card_issuer_bank_id=None,       # type: Optional[int]
        force3ds=None,                  # type: Optional[bool]
        pos=None,                       # type: Optional[MerchantPos]
        loyalties=None                  # type: Optional[List[Loyalty]]
    ):
        self.card_brand = card_brand
        self.card_issuer_bank_name = card_issuer_bank_name
        self.card_issuer_bank_id = card_issuer_bank_id
        self.force3ds = force3ds
        self.pos = pos
        self.loyalties = loyalties