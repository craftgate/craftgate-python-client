from typing import Optional
from craftgate.model.payment_status import PaymentStatus
from craftgate.response.dto.payment_error import PaymentError

class ApmPaymentCompleteResponse(object):
    def __init__(
        self,
        payment_id=None,              # type: Optional[int]
        payment_status=None,          # type: Optional[PaymentStatus]
        payment_error=None             # type: Optional[PaymentError]
    ):
        self.payment_id = payment_id
        self.payment_status = payment_status
        self.payment_error = payment_error