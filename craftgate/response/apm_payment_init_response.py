from typing import Optional, Dict, Any
from craftgate.model.apm_additional_action import ApmAdditionalAction
from craftgate.model.payment_status import PaymentStatus
from craftgate.response.dto.payment_error import PaymentError

class ApmPaymentInitResponse(object):
    def __init__(
        self,
        payment_id=None,              # type: Optional[int]
        redirect_url=None,             # type: Optional[str]
        html_content=None,              # type: Optional[str]
        payment_status=None,           # type: Optional[PaymentStatus]
        additional_action=None,        # type: Optional[ApmAdditionalAction]
        payment_error=None,             # type: Optional[PaymentError]
        additional_data=None            # type: Optional[Dict[str, Any]]
    ):
        self.payment_id = payment_id
        self.redirect_url = redirect_url
        self.html_content = html_content
        self.payment_status = payment_status
        self.additional_action = additional_action
        self.payment_error = payment_error
        self.additional_data = additional_data