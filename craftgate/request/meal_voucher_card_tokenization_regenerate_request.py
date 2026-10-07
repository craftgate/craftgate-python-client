from typing import Optional
from craftgate.request.common.base_request import BaseRequest
from craftgate.request.dto.meal_voucher_card_tokenization_data import MealVoucherCardTokenizationData


class MealVoucherCardTokenizationRegenerateRequest(BaseRequest):
    def __init__(
        self,
        meal_voucher_card_tokenization_data: Optional[MealVoucherCardTokenizationData] = None
    ) -> None:
        self.meal_voucher_card_tokenization_data = meal_voucher_card_tokenization_data
