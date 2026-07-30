from typing import Optional


class MealVoucherCardTokenizationData:
    def __init__(
        self,
        card_number: Optional[str] = None,
        user_reference_number: Optional[str] = None,
        gsm_number: Optional[str] = None,
        callback_url: Optional[str] = None
    ) -> None:
        self.card_number = card_number
        self.user_reference_number = user_reference_number
        self.gsm_number = gsm_number
        self.callback_url = callback_url
