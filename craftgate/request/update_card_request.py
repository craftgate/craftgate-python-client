from typing import Optional


class UpdateCardRequest(object):
    def __init__(
        self,
        card_user_key: Optional[str] = None,
        card_token: Optional[str] = None,
        expire_year: Optional[str] = None,
        expire_month: Optional[str] = None,
        card_alias: Optional[str] = None
    ) -> None:
        self.card_user_key = card_user_key
        self.card_token = card_token
        self.expire_year = expire_year
        self.expire_month = expire_month
        self.card_alias = card_alias
