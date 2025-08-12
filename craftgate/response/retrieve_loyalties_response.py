from typing import List, Optional

from craftgate.model.fraud_result import FraudResult
from craftgate.model.loyalty import Loyalty
from craftgate.response.dto.merchant_pos import MerchantPos


class RetrieveLoyaltiesResponse(object):
    def __init__(
            self,
            card_brand: Optional[str] = None,
            card_issuer_bank_name: Optional[str] = None,
            card_issuer_bank_id: Optional[int] = None,
            force3ds: Optional[bool] = None,
            pos: Optional[MerchantPos] = None,
            loyalties: Optional[List[Loyalty]] = None,
            fraud_result: Optional[FraudResult] = None
    ) -> None:
        self.card_brand = card_brand
        self.card_issuer_bank_name = card_issuer_bank_name
        self.card_issuer_bank_id = card_issuer_bank_id
        self.force3ds = force3ds
        self.pos = pos
        self.loyalties = loyalties
        self.fraud_result = fraud_result
