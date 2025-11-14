from typing import Optional

from craftgate.model.fraud_action import FraudAction


class FraudResult:
    def __init__(
            self,
            id: Optional[int] = None,
            score: Optional[float] = None,
            action: Optional[FraudAction] = None
    ) -> None:
        self.id = id
        self.score = score
        self.action = action