from typing import Optional, Dict, Any

from craftgate.model.tokenized_card_type import TokenizedCardType


class TokenizedCard(object):
    def __init__(
            self,
            type: Optional[TokenizedCardType] = None,
            data: Optional[Dict[str, Any]] = None
    ) -> None:
        self.type = type
        self.data = data
