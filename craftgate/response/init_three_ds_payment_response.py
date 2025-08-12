from typing import Optional
import base64
from craftgate.model.payment_status import PaymentStatus
from craftgate.model.additional_action import AdditionalAction

class InitThreeDSPaymentResponse(object):
    def __init__(
        self,
        html_content=None,            # type: Optional[str]
        payment_id=None,              # type: Optional[int]
        redirect_url=None,             # type: Optional[str]
        payment_status=None,           # type: Optional[PaymentStatus]
        additional_action=None         # type: Optional[AdditionalAction]
    ):
        self.html_content = html_content
        self.payment_id = payment_id
        self.redirect_url = redirect_url
        self.payment_status = payment_status
        self.additional_action = additional_action

    def get_decoded_html_content(self):
        if self.html_content is None:
            return None
        return base64.b64decode(self.html_content).decode("utf-8")