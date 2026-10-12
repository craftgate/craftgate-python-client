from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class MealVoucherCardTokenizationCompleteRequest(BaseRequest):
    def __init__(
        self,
        validation_code: Optional[str] = None
    ) -> None:
        self.validation_code = validation_code
