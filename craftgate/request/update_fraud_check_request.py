from typing import Optional

from craftgate.model.fraud_check_status import FraudCheckStatus
from craftgate.request.common.base_request import BaseRequest


class UpdateFraudCheckRequest(BaseRequest):
    def __init__(self, check_status: Optional[FraudCheckStatus] = None) -> None:
        self.check_status = check_status
