from typing import Optional


class CreatePaymentTokenRequest(object):
    def __init__(
            self,
            value: Optional[str] = None,
            issuer: Optional[str] = None
    ) -> None:
        self.value = value
        self.issuer = issuer
