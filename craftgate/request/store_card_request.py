from typing import Optional

from craftgate.request.dto.encrypted_card import EncryptedCard


class StoreCardRequest(object):
    def __init__(
            self,
            card_holder_name: Optional[str] = None,
            card_number: Optional[str] = None,
            expire_year: Optional[str] = None,
            expire_month: Optional[str] = None,
            secure_fields_token: Optional[str] = None,
            card_alias: Optional[str] = None,
            card_user_key: Optional[str] = None,
            encrypted_card: Optional[EncryptedCard] = None
    ) -> None:
        self.card_holder_name = card_holder_name
        self.card_number = card_number
        self.expire_year = expire_year
        self.expire_month = expire_month
        self.secure_fields_token = secure_fields_token
        self.card_alias = card_alias
        self.card_user_key = card_user_key
        self.encrypted_card = encrypted_card
