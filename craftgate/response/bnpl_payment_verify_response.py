from typing import Optional

from craftgate.model.apm_additional_action import ApmAdditionalAction
from craftgate.model.payment_status import PaymentStatus
from craftgate.response.dto.payment_error import PaymentError


class BnplPaymentVerifyResponse(object):
    def __init__(
            self,
            payment_status: Optional[PaymentStatus] = None,
            additional_action: Optional[ApmAdditionalAction] = None,
            payment_error: Optional[PaymentError] = None
    ) -> None:
        self.payment_status = payment_status
        self.additional_action = additional_action
        self.payment_error = payment_error
