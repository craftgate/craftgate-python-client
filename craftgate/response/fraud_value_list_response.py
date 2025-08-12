from typing import List, Optional

from craftgate.model.fraud_value import FraudValue


class FraudValueListResponse(object):
    def __init__(
            self,
            name: Optional[str] = None,
            values: Optional[List[FraudValue]] = None
    ) -> None:
        self.name = name
        self.values = values or []
