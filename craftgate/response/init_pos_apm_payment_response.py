from typing import Optional, Dict, Any
from craftgate.model.payment_status import PaymentStatus
from craftgate.model.additional_action import AdditionalAction
from craftgate.response.dto.payment_error import PaymentError

class InitPosApmPaymentResponse(object):
    def __init__(
        self,
        html_content=None,            # type: Optional[str]
        payment_id=None,              # type: Optional[int]
        payment_status=None,          # type: Optional[PaymentStatus]
        additional_action=None,       # type: Optional[AdditionalAction]
        payment_error=None,           # type: Optional[PaymentError]
        additional_data=None          # type: Optional[Dict[str, Any]]
    ):
        self.html_content = html_content
        self.payment_id = payment_id
        self.payment_status = payment_status
        self.additional_action = additional_action
        self.payment_error = payment_error
        self.additional_data = additional_data