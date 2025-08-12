from typing import Optional
from datetime import datetime

class InitCheckoutPaymentResponse(object):
    def __init__(
        self,
        token=None,                # type: Optional[str]
        page_url=None,              # type: Optional[str]
        token_expire_date=None      # type: Optional[datetime]
    ):
        self.token = token
        self.page_url = page_url
        self.token_expire_date = token_expire_date