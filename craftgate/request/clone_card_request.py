from typing import Optional


class CloneCardRequest(object):
    def __init__(
            self,
            source_card_user_key: Optional[str] = None,
            source_card_token: Optional[str] = None,
            target_card_user_key: Optional[str] = None,
            target_merchant_id: Optional[int] = None
    ) -> None:
        self.source_card_user_key = source_card_user_key
        self.source_card_token = source_card_token
        self.target_card_user_key = target_card_user_key
        self.target_merchant_id = target_merchant_id
