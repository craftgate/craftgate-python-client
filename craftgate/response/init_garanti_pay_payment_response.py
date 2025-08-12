import base64
from typing import Optional


class InitGarantiPayPaymentResponse(object):
    def __init__(
            self,
            html_content: Optional[str] = None,
            payment_id: Optional[int] = None
    ) -> None:
        self.html_content = html_content
        self.payment_id = payment_id

    def get_decoded_html_content(self) -> Optional[str]:
        if self.html_content is None:
            return None
        return base64.b64decode(self.html_content).decode("utf-8")
