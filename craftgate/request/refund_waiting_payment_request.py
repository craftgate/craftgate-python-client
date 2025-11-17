from typing import Optional

class RefundWaitingPaymentRequest(object):
    def __init__(
            self,
            payment_id: Optional[int] = None
    ) -> None:
        self.payment_id = payment_id