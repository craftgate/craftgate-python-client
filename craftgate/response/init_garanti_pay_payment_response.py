from typing import Optional
import base64

class InitGarantiPayPaymentResponse(object):
    def __init__(
        self,
        html_content=None,      # type: Optional[str]
        payment_id=None         # type: Optional[int]
    ):
        self.html_content = html_content
        self.payment_id = payment_id

    def get_decoded_html_content(self):
        if self.html_content is None:
            return None
        return base64.b64decode(self.html_content).decode("utf-8")