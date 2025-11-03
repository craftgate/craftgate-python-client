from datetime import datetime
from typing import Optional

from craftgate.model.card_association import CardAssociation
from craftgate.model.card_expiry_status import CardExpiryStatus
from craftgate.model.card_type import CardType


class StoredCardResponse(object):
    def __init__(
            self,
            bin_number: Optional[str] = None,
            last_four_digits: Optional[str] = None,
            card_user_key: Optional[str] = None,
            card_token: Optional[str] = None,
            card_holder_name: Optional[str] = None,
            card_alias: Optional[str] = None,
            card_type: Optional[CardType] = None,
            card_association: Optional[CardAssociation] = None,
            card_brand: Optional[str] = None,
            card_bank_name: Optional[str] = None,
            card_bank_id: Optional[int] = None,
            is_commercial: Optional[bool] = None,
            card_expiry_status: Optional[CardExpiryStatus] = None,
            created_at: Optional[datetime] = None
    ) -> None:
        self.bin_number = bin_number
        self.last_four_digits = last_four_digits
        self.card_user_key = card_user_key
        self.card_token = card_token
        self.card_holder_name = card_holder_name
        self.card_alias = card_alias
        self.card_type = card_type
        self.card_association = card_association
        self.card_brand = card_brand
        self.card_bank_name = card_bank_name
        self.card_bank_id = card_bank_id
        self.is_commercial = is_commercial
        self.card_expiry_status = card_expiry_status
        self.created_at = created_at
