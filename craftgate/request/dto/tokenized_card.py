from typing import Optional, Dict, Any

from craftgate.model.tokenized_card_type import TokenizedCardType


class TokenizedCard(object):
    def __init__(self,
                 type=None,  # type: Optional[TokenizedCardType]
                 data=None  # type: Optional[Dict[str, Any]]
                 ):
        self.type = type
        self.data = data
