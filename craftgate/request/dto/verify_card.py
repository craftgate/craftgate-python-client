from typing import Optional


class VerifyCard(object):
    def __init__(
            self,
            card_holder_name: Optional[str] = None,
            card_number: Optional[str] = None,
            expire_year: Optional[str] = None,
            expire_month: Optional[str] = None,
            cvc: Optional[str] = None,
            card_alias: Optional[str] = None,
            card_user_key: Optional[str] = None
    ) -> None:
        self.card_holder_name = card_holder_name
        self.card_number = card_number
        self.expire_year = expire_year
        self.expire_month = expire_month
        self.cvc = cvc
        self.card_alias = card_alias
        self.card_user_key = card_user_key
