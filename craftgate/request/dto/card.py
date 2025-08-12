from typing import Optional

from craftgate.model.loyalty import Loyalty
from craftgate.request.dto.tokenized_card import TokenizedCard


class Card(object):
    def __init__(self,
                 card_holder_name=None,  # type: Optional[str]
                 card_number=None,  # type: Optional[str]
                 expire_year=None,  # type: Optional[str]
                 expire_month=None,  # type: Optional[str]
                 cvc=None,  # type: Optional[str]
                 card_alias=None,  # type: Optional[str]
                 card_user_key=None,  # type: Optional[str]
                 card_token=None,  # type: Optional[str]
                 bin_number=None,  # type: Optional[str]
                 last_four_digits=None,  # type: Optional[str]
                 card_holder_identity_number=None,  # type: Optional[str]
                 loyalty=None,  # type: Optional[Loyalty]
                 tokenized_card=None,  # type: Optional[TokenizedCard]
                 store_card_after_success_payment=False  # type: bool
                 ):
        self.card_holder_name = card_holder_name
        self.card_number = card_number
        self.expire_year = expire_year
        self.expire_month = expire_month
        self.cvc = cvc
        self.card_alias = card_alias
        self.card_user_key = card_user_key
        self.card_token = card_token
        self.bin_number = bin_number
        self.last_four_digits = last_four_digits
        self.card_holder_identity_number = card_holder_identity_number
        self.loyalty = loyalty
        self.tokenized_card = tokenized_card
        self.store_card_after_success_payment = store_card_after_success_payment
