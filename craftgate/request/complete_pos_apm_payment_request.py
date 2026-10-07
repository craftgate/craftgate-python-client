from typing import Any, Dict, Optional

from craftgate.request.common.base_request import BaseRequest


class CompletePosApmPaymentRequest(BaseRequest):
    def __init__(
            self,
            payment_id: Optional[int] = None,
            additional_params: Optional[Dict[str, Any]] = None
    ) -> None:
        self.payment_id = payment_id
        self.additional_params = additional_params
