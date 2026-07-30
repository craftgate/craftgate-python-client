from typing import Optional
from craftgate.request.dto.meal_voucher_card_tokenization_data import MealVoucherCardTokenizationData


class MealVoucherCardTokenizationRegenerateRequest:
    def __init__(
        self,
        meal_voucher_card_tokenization_data: Optional[MealVoucherCardTokenizationData] = None
    ) -> None:
        self.meal_voucher_card_tokenization_data = meal_voucher_card_tokenization_data
