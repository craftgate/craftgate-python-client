from typing import Any, Dict, Optional

from craftgate.model.apm_additional_action import ApmAdditionalAction
from craftgate.model.payment_status import PaymentStatus
from craftgate.response.dto.payment_error import PaymentError


class ApmPaymentInitResponse(object):
    def __init__(
            self,
            payment_id: Optional[int] = None,
            redirect_url: Optional[str] = None,
            html_content: Optional[str] = None,
            payment_status: Optional[PaymentStatus] = None,
            additional_action: Optional[ApmAdditionalAction] = None,
            payment_error: Optional[PaymentError] = None,
            additional_data: Optional[Dict[str, Any]] = None
    ) -> None:
        self.payment_id = payment_id
        self.redirect_url = redirect_url
        self.html_content = html_content
        self.payment_status = payment_status
        self.additional_action = additional_action
        self.payment_error = payment_error
        self.additional_data = additional_data
