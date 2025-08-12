from typing import Optional

from craftgate.model.fraud_check_status import FraudCheckStatus


class UpdateFraudCheckRequest(object):
    def __init__(self, check_status: Optional[FraudCheckStatus] = None) -> None:
        self.check_status = check_status
