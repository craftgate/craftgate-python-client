from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class MasterpassPaymentThreeDSInitRequest(BaseRequest):
    def __init__(
            self,
            reference_id: Optional[str] = None,
            callback_url: Optional[str] = None
    ) -> None:
        self.reference_id = reference_id
        self.callback_url = callback_url
