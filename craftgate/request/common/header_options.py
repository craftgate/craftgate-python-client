from typing import Optional

class HeaderOptions(object):

    def __init__(self, idempotency_key: Optional[str] = None) -> None:
        self.idempotency_key = idempotency_key
