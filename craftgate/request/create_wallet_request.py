from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.request.common.base_request import BaseRequest


class CreateWalletRequest(BaseRequest):
    def __init__(
            self,
            negative_amount_limit: Optional[Decimal] = None,
            currency: Optional[Currency] = None
    ) -> None:
        self.negative_amount_limit = negative_amount_limit
        self.currency = currency
