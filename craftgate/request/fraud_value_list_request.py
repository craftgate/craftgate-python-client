from typing import Optional

from craftgate.model.fraud_value_type import FraudValueType


class FraudValueListRequest(object):
    def __init__(
            self,
            list_name: Optional[str] = None,
            label: Optional[str] = None,
            type: Optional[FraudValueType] = None,
            value: Optional[str] = None,
            duration_in_seconds: Optional[int] = None,
            payment_id: Optional[int] = None
    ) -> None:
        self.list_name = list_name
        self.label = label
        self.type = type
        self.value = value
        self.duration_in_seconds = duration_in_seconds
        self.payment_id = payment_id
