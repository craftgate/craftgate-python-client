from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class CreatePaymentTokenRequest(BaseRequest):
    def __init__(
            self,
            value: Optional[str] = None,
            issuer: Optional[str] = None
    ) -> None:
        self.value = value
        self.issuer = issuer
