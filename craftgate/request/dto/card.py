from typing import Optional

from craftgate.model.loyalty import Loyalty
from craftgate.request.dto.tokenized_card import TokenizedCard
from craftgate.request.dto.encrypted_card import EncryptedCard


class Card(object):
    def __init__(
            self,
            card_holder_name: Optional[str] = None,
            card_number: Optional[str] = None,
            expire_year: Optional[str] = None,
            expire_month: Optional[str] = None,
            cvc: Optional[str] = None,
            card_alias: Optional[str] = None,
            card_user_key: Optional[str] = None,
            secure_fields_token: Optional[str] = None,
            card_token: Optional[str] = None,
            bin_number: Optional[str] = None,
            last_four_digits: Optional[str] = None,
            card_holder_identity_number: Optional[str] = None,
            loyalty: Optional[Loyalty] = None,
            tokenized_card: Optional[TokenizedCard] = None,
            encrypted_card: Optional[EncryptedCard] = None,
            store_card_after_success_payment: bool = False
    ) -> None:
        self.card_holder_name = card_holder_name
        self.card_number = card_number
        self.expire_year = expire_year
        self.expire_month = expire_month
        self.cvc = cvc
        self.card_alias = card_alias
        self.card_user_key = card_user_key
        self.secure_fields_token = secure_fields_token
        self.card_token = card_token
        self.bin_number = bin_number
        self.last_four_digits = last_four_digits
        self.card_holder_identity_number = card_holder_identity_number
        self.loyalty = loyalty
        self.tokenized_card = tokenized_card
        self.encrypted_card = encrypted_card
        self.store_card_after_success_payment = store_card_after_success_payment
