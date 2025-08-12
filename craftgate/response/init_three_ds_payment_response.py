import base64
from typing import Optional

from craftgate.model.additional_action import AdditionalAction
from craftgate.model.payment_status import PaymentStatus


class InitThreeDSPaymentResponse(object):
    def __init__(
            self,
            html_content: Optional[str] = None,
            payment_id: Optional[int] = None,
            redirect_url: Optional[str] = None,
            payment_status: Optional[PaymentStatus] = None,
            additional_action: Optional[AdditionalAction] = None
    ) -> None:
        self.html_content = html_content
        self.payment_id = payment_id
        self.redirect_url = redirect_url
        self.payment_status = payment_status
        self.additional_action = additional_action

    def get_decoded_html_content(self) -> Optional[str]:
        if self.html_content is None:
            return None
        return base64.b64decode(self.html_content).decode("utf-8")
