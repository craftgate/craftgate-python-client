from typing import Optional

from craftgate.model import RefundStatus


class WaitingPaymentRefundResponse(object):
    def __init__(
            self,
            status: Optional[RefundStatus] = None,
    ) -> None:
        self.status = status
