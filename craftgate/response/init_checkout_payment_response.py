from datetime import datetime
from typing import Optional


class InitCheckoutPaymentResponse(object):
    def __init__(
            self,
            token: Optional[str] = None,
            page_url: Optional[str] = None,
            token_expire_date: Optional[datetime] = None
    ) -> None:
        self.token = token
        self.page_url = page_url
        self.token_expire_date = token_expire_date
