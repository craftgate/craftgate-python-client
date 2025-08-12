from typing import Optional
from craftgate.model.card_provider import CardProvider

class RetrieveProviderCardRequest(object):
    def __init__(
        self,
        provider_card_token=None,    # type: Optional[str]
        external_id=None,            # type: Optional[str]
        provider_card_user_id=None,  # type: Optional[str]
        card_provider=None           # type: Optional[CardProvider]
    ):
        self.provider_card_token = provider_card_token
        self.external_id = external_id
        self.provider_card_user_id = provider_card_user_id
        self.card_provider = card_provider