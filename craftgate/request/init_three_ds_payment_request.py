from typing import Any, Optional

from craftgate.request.create_payment_request import CreatePaymentRequest


class InitThreeDSPaymentRequest(CreatePaymentRequest):
    def __init__(
            self,
            callback_url: Optional[str] = None,
            **kwargs: Any
    ) -> None:
        super().__init__(**kwargs)
        self.callback_url = callback_url
