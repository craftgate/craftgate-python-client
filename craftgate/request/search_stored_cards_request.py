from datetime import datetime
from typing import Optional

from craftgate.model.card_association import CardAssociation
from craftgate.model.card_expiry_status import CardExpiryStatus
from craftgate.model.card_type import CardType


class SearchStoredCardsRequest(object):
    def __init__(
            self,
            card_alias: Optional[str] = None,
            card_brand: Optional[str] = None,
            card_type: Optional[CardType] = None,
            card_user_key: Optional[str] = None,
            card_token: Optional[str] = None,
            card_bank_name: Optional[str] = None,
            card_association: Optional[CardAssociation] = None,
            card_expiry_status: Optional[CardExpiryStatus] = None,
            min_created_date: Optional[datetime] = None,
            max_created_date: Optional[datetime] = None,
            page: int = 0,
            size: int = 10
    ) -> None:
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
