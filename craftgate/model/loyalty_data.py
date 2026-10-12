from typing import Optional


class LoyaltyData:
    def __init__(
            self,
            max_postponing_payment_count: Optional[int] = None,
            unit_type: Optional[str] = None,
            code: Optional[str] = None
    ) -> None:
        self.max_postponing_payment_count = max_postponing_payment_count
        self.unit_type = unit_type
        self.code = code