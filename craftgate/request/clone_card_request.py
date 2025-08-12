from typing import Optional


class CloneCardRequest(object):
    def __init__(self,
                 source_card_user_key=None,  # type: Optional[str]
                 source_card_token=None,  # type: Optional[str]
                 target_card_user_key=None,  # type: Optional[str]
                 target_merchant_id=None  # type: Optional[int]
                 ):
        self.source_card_user_key = source_card_user_key
        self.source_card_token = source_card_token
        self.target_card_user_key = target_card_user_key
        self.target_merchant_id = target_merchant_id
