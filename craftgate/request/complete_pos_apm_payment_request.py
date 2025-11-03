from typing import Any, Dict, Optional


class CompletePosApmPaymentRequest(object):
    def __init__(
            self,
            payment_id: Optional[int] = None,
            additional_params: Optional[Dict[str, Any]] = None
    ) -> None:
        self.payment_id = payment_id
        self.additional_params = additional_params
