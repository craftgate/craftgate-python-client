from typing import Optional, List

from craftgate.model.fraud_value import FraudValue


class FraudValueListResponse(object):
    def __init__(self):
        # type: () -> None
        self.name = None  # type: Optional[str]
        self.values = []  # type: List[FraudValue]
