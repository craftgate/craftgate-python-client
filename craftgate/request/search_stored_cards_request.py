from typing import Optional
from datetime import datetime
from craftgate.model.card_type import CardType
from craftgate.model.card_association import CardAssociation
from craftgate.model.card_expiry_status import CardExpiryStatus

class SearchStoredCardsRequest(object):
    def __init__(
        self,
        card_alias=None,               # type: Optional[str]
        card_brand=None,               # type: Optional[str]
        card_type=None,                 # type: Optional[CardType]
        card_user_key=None,             # type: Optional[str]
        card_token=None,                # type: Optional[str]
        card_bank_name=None,            # type: Optional[str]
        card_association=None,          # type: Optional[CardAssociation]
        card_expiry_status=None,        # type: Optional[CardExpiryStatus]
        min_created_date=None,          # type: Optional[datetime]
        max_created_date=None,          # type: Optional[datetime]
        page=0,                         # type: int
        size=10                         # type: int
    ):
        self.card_alias = card_alias
        self.card_brand = card_brand
        self.card_type = card_type
        self.card_user_key = card_user_key
        self.card_token = card_token
        self.card_bank_name = card_bank_name
        self.card_association = card_association
        self.card_expiry_status = card_expiry_status
        self.min_created_date = min_created_date
        self.max_created_date = max_created_date
        self.page = page
        self.size = size