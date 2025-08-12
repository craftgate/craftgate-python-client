from decimal import Decimal
from typing import Optional


class PosApmInstallment(object):
    def __init__(
            self,
            number: Optional[int] = None,
            total_price: Optional[Decimal] = None
    ) -> None:
        self.number = number
        self.total_price = total_price
