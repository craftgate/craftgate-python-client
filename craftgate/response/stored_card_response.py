from craftgate.model.card_type import CardType
from craftgate.model.card_association import CardAssociation
from craftgate.model.card_expiry_status import CardExpiryStatus

class StoredCardResponse(object):
    def __init__(
        self, bin_number=None, last_four_digits=None, card_user_key=None, card_token=None,
        card_holder_name=None, card_alias=None, card_type=None, card_association=None,
        card_brand=None, card_bank_name=None, card_bank_id=None, card_expiry_status=None,
        created_at=None
    ):
        self.bin_number = bin_number
        self.last_four_digits = last_four_digits
        self.card_user_key = card_user_key
        self.card_token = card_token
        self.card_holder_name = card_holder_name
        self.card_alias = card_alias
        self.card_type = CardType(card_type) if card_type else None
        self.card_association = CardAssociation(card_association) if card_association else None
        self.card_brand = card_brand
        self.card_bank_name = card_bank_name
        self.card_bank_id = card_bank_id
        self.card_expiry_status = CardExpiryStatus(card_expiry_status) if card_expiry_status else None
        self.created_at = created_at