from typing import Optional

from craftgate.model.fraud_operation import FraudOperation


class FraudAddCardFingerprintToListRequest(object):
    def __init__(
            self,
            label: Optional[str] = None,
            operation: Optional[FraudOperation] = None,
            operation_id: Optional[str] = None,
            duration_in_seconds: Optional[int] = None
    ) -> None:
        self.label = label
        self.operation = operation
        self.operation_id = operation_id
        self.duration_in_seconds = duration_in_seconds
