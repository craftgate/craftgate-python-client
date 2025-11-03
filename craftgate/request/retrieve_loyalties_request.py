from typing import Optional


class RetrieveLoyaltiesRequest(object):
    def __init__(
            self,
            card_number: Optional[str] = None,
            expire_year: Optional[str] = None,
            expire_month: Optional[str] = None,
            cvc: Optional[str] = None,
            card_user_key: Optional[str] = None,
            card_token: Optional[str] = None
    ) -> None:
        self.card_number = card_number
        self.expire_year = expire_year
        self.expire_month = expire_month
        self.cvc = cvc
        self.card_user_key = card_user_key
        self.card_token = card_token
