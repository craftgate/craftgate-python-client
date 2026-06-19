from typing import Optional

from craftgate.model.apm_type import ApmType
from craftgate.request.dto.meal_voucher_card_tokenization_data import MealVoucherCardTokenizationData


class InitMealVoucherCardTokenizationRequest:
    def __init__(
        self,
        apm_type: Optional[ApmType] = None,
        meal_voucher_card_tokenization_data: Optional[MealVoucherCardTokenizationData] = None
    ) -> None:
        self.apm_type = apm_type
        self.meal_voucher_card_tokenization_data = meal_voucher_card_tokenization_data
