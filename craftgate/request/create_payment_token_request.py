from typing import Optional


class CreatePaymentTokenRequest(object):
    def __init__(
            self,
            value=None,  # type: Optional[str]
            issuer=None  # type: Optional[str]
    ):
        self.value = value
        self.issuer = issuer
