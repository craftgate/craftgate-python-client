from typing import Optional


class LoyaltyParams:
    def __init__(
            self,
            postponing_payment_count: Optional[int] = None
    ) -> None:
        self.postponing_payment_count = postponing_payment_count
