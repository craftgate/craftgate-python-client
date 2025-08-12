from typing import Optional

class PostAuthPaymentRequest(object):
    def __init__(self, paid_price=None):
        # type: (Optional[float]) -> None
        self.paid_price = paid_price