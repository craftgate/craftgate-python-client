from typing import Any, Dict, Optional

from craftgate.model.apm_additional_action import ApmAdditionalAction
from craftgate.model.payment_status import PaymentStatus
from craftgate.response.dto.payment_error import PaymentError


class BnplLimitInquiryResponse(object):
    def __init__(
            self,
            payment_status: Optional[PaymentStatus] = None,
            additional_action: Optional[ApmAdditionalAction] = None,
            errorCode: Optional[str] = None,
            errorMessage: Optional[str] = None,
            additional_data: Optional[Dict[str, Any]] = None
    ) -> None:
        self.payment_status = payment_status
        self.additional_action = additional_action
        self.additional_data = additional_data
        self.errorCode = errorCode
        self.errorMessage = errorMessage
