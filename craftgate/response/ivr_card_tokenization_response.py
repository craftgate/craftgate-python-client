from typing import Optional

class IVRCardTokenizationResponse(object):
    def __init__(
            self,
            bin_number: Optional[str] = None,
            last_four_digits: Optional[str] = None,
            card_user_key: Optional[str] = None,
            card_token: Optional[str] = None,
            secure_fields_token: Optional[str] = None
    ) -> None:
        self.bin_number = bin_number
        self.last_four_digits = last_four_digits
        self.card_user_key = card_user_key
        self.card_token = card_token
        self.secure_fields_token = secure_fields_token
