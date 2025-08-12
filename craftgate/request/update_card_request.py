from typing import Optional

class UpdateCardRequest(object):
    def __init__(
        self,
        card_user_key=None,  # type: Optional[str]
        card_token=None,     # type: Optional[str]
        expire_year=None,    # type: Optional[str]
        expire_month=None    # type: Optional[str]
    ):
        self.card_user_key = card_user_key
        self.card_token = card_token
        self.expire_year = expire_year
        self.expire_month = expire_month