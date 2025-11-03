from typing import Optional


class DeleteStoredCardRequest(object):
    def __init__(
            self,
            card_user_key: Optional[str] = None,
            card_token: Optional[str] = None
    ) -> None:
        self.card_user_key = card_user_key
        self.card_token = card_token
