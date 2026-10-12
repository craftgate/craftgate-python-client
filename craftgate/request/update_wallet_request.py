from decimal import Decimal
from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class UpdateWalletRequest(BaseRequest):
    def __init__(self, negative_amount_limit: Optional[Decimal] = None):
        self.negative_amount_limit = negative_amount_limit
