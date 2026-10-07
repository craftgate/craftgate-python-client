from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class VerifyBnplPaymentRequest(BaseRequest):
    def __init__(
            self,
            payment_id: Optional[int] = None
    ) -> None:
        self.payment_id = payment_id
