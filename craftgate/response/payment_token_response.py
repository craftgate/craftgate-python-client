from typing import Optional


class PaymentTokenResponse(object):
    def __init__(
            self,
            token: Optional[str] = None,
            issuer: Optional[str] = None
    ) -> None:
        self.token = token
        self.issuer = issuer
