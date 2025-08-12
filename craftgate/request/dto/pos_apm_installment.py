from typing import Optional


class PosApmInstallment(object):
    def __init__(
            self,
            number=None,  # type: Optional[int]
            total_price=None  # type: Optional[float]
    ):
        self.number = number
        self.total_price = total_price
