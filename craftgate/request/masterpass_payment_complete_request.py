from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class MasterpassPaymentCompleteRequest(BaseRequest):
    def __init__(
            self,
            reference_id: Optional[str] = None,
            token: Optional[str] = None
    ) -> None:
        self.reference_id = reference_id
        self.token = token
