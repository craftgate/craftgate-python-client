from datetime import datetime
from typing import Optional

from craftgate.model.fraud_action import FraudAction
from craftgate.model.fraud_operation import FraudOperation

class SearchFraudRuleRequest(object):
    def __init__(
            self,
            name: Optional[str] = None,
            min_created_date: Optional[datetime] = None,
            max_created_date: Optional[datetime] = None,
            action: Optional[FraudAction] = None,
            operation: Optional[FraudOperation] = None,
            page: Optional[int] = None,
            size: Optional[int] = None,
    ) -> None:
        self.page = page
        self.size = size
        self.action = action
        self.operation = operation
        self.name = name
        self.min_created_date = min_created_date
        self.max_created_date = max_created_date
