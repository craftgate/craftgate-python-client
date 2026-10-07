from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class ExpireCheckoutPaymentRequest(BaseRequest):
    def __init__(
            self,
            token: Optional[str] = None
    ) -> None:
        self.token = token
