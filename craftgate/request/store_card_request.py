from typing import Optional

class StoreCardRequest(object):
    def __init__(
        self,
        card_holder_name=None,  # type: Optional[str]
        card_number=None,       # type: Optional[str]
        expire_year=None,       # type: Optional[str]
        expire_month=None,      # type: Optional[str]
        card_alias=None,        # type: Optional[str]
        card_user_key=None      # type: Optional[str]
    ):
        self.card_holder_name = card_holder_name
        self.card_number = card_number
        self.expire_year = expire_year
        self.expire_month = expire_month
        self.card_alias = card_alias
        self.card_user_key = card_user_key