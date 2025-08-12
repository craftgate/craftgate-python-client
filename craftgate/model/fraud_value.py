from typing import Optional


class FraudValue(object):
    def __init__(
            self,
            id: Optional[str] = None,
            label: Optional[str] = None,
            value: Optional[str] = None,
            expire_in_seconds: Optional[int] = None
    ) -> None:
        self.id = id
        self.label = label
        self.value = value
        self.expire_in_seconds = expire_in_seconds
