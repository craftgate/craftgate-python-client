from typing import Optional

from craftgate.model.fraud_check_status import FraudCheckStatus
from craftgate.request.common.base_request import BaseRequest


class UpdateFraudCheckStatusRequest(BaseRequest):
    def __init__(
            self,
            id: Optional[int] = None,
            check_status: Optional[FraudCheckStatus] = None
    ) -> None:
        self.id = id
        self.check_status = check_status
