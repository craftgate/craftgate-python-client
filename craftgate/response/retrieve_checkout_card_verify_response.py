from typing import Optional

from craftgate.response.stored_card_response import StoredCardResponse


class RetrieveCheckoutCardVerifyResponse(object):
    def __init__(
            self,
            token: Optional[str] = None,
            card: Optional[StoredCardResponse] = None
    ) -> None:
        self.token = token
        self.card = card
