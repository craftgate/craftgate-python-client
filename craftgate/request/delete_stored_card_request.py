from typing import Optional

class DeleteStoredCardRequest(object):
    def __init__(self,
                 card_user_key=None,  # type: Optional[str]
                 card_token=None      # type: Optional[str]
                 ):
        self.card_user_key = card_user_key
        self.card_token = card_token