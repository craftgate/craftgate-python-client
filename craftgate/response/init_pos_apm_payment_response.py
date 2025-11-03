from typing import Any, Dict, Optional

from craftgate.model.additional_action import AdditionalAction
from craftgate.model.payment_status import PaymentStatus
from craftgate.response.dto.payment_error import PaymentError


class InitPosApmPaymentResponse(object):
    def __init__(
            self,
            html_content: Optional[str] = None,
            payment_id: Optional[int] = None,
            payment_status: Optional[PaymentStatus] = None,
            additional_action: Optional[AdditionalAction] = None,
            payment_error: Optional[PaymentError] = None,
            additional_data: Optional[Dict[str, Any]] = None
    ) -> None:
        self.html_content = html_content
        self.payment_id = payment_id
        self.payment_status = payment_status
        self.additional_action = additional_action
        self.payment_error = payment_error
        self.additional_data = additional_data
