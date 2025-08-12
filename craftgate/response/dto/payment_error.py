from typing import Optional


class PaymentError:
    def __init__(
        self,
        error_code: Optional[str] = None,
        error_description: Optional[str] = None,
        error_group: Optional[str] = None
    ) -> None:
        self.error_code = error_code
        self.error_description = error_description
        self.error_group = error_group
