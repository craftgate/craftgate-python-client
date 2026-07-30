from typing import Optional


class MealVoucherCardTokenizationCompleteRequest:
    def __init__(
        self,
        validation_code: Optional[str] = None
    ) -> None:
        self.validation_code = validation_code
