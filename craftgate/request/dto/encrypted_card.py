from typing import Optional


class EncryptedCard(object):
    def __init__(
            self,
            card_data: Optional[str] = None,
            type: Optional[str] = None
    ) -> None:
        self.card_data = card_data
        self.type = type
