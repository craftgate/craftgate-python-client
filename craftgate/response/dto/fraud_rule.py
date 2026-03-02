from typing import Optional, List

from craftgate.model.fraud_action import FraudAction
from craftgate.model.fraud_operation import FraudOperation
from craftgate.model.status import Status

class FraudRule(object):
    def __init__(
            self,
            id: Optional[int] = None,
            status: Optional[Status] = None,
            name: Optional[str] = None,
            action: Optional[FraudAction] = None,
            conditions: Optional[str] = None,
            operations: Optional[List[FraudOperation]] = None
    ) -> None:
        self.id = id
        self.status = status
        self.action = action
        self.name = name
        self.conditions = conditions
        self.operations = operations
