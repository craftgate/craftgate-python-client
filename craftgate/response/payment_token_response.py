from typing import Optional


class PaymentTokenResponse(object):
    def __init__(
        self,
        token=None,   # type: Optional[str]
        issuer=None   # type: Optional[str]
    ):
        self.token = token
        self.issuer = issuer
