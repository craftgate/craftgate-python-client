from typing import Optional

from craftgate.model.card_verify_status import CardVerifyStatus
from craftgate.model.refund_status import RefundStatus


class VerifyCardResponse(object):
    def __init__(
            self,
            card_user_key: Optional[str] = None,
            card_token: Optional[str] = None,
            html_content: Optional[str] = None,
            redirect_url: Optional[str] = None,
            merchant_callback_url: Optional[str] = None,
            refund_status: Optional[RefundStatus] = None,
            card_verify_status: Optional[CardVerifyStatus] = None
    ) -> None:
        self.card_user_key = card_user_key
        self.card_token = card_token
        self.html_content = html_content
        self.redirect_url = redirect_url
        self.merchant_callback_url = merchant_callback_url
        self.refund_status = refund_status
        self.card_verify_status = card_verify_status
