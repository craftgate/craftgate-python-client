from decimal import Decimal
from typing import Optional


class UpdateWalletRequest(object):
    def __init__(self, negative_amount_limit: Optional[Decimal] = None):
        self.negative_amount_limit = negative_amount_limit
