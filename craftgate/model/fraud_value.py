class FraudValue(object):
    def __init__(self, id=None, label=None, value=None, expire_in_seconds=None):
        # type: (Optional[str], Optional[str], Optional[str], Optional[int]) -> None
        self.id = id
        self.label = label
        self.value = value
        self.expire_in_seconds = expire_in_seconds
