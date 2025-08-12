from typing import Optional


class CustomInstallment(object):
    def __init__(self, number=None, total_price=None):
        # type: (Optional[int], Optional[float]) -> None
        self.number = number
        self.total_price = total_price
