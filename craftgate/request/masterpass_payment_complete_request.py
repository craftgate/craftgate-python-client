from typing import Optional


class MasterpassPaymentCompleteRequest(object):
    def __init__(
            self,
            reference_id: Optional[str] = None,
            token: Optional[str] = None
    ) -> None:
        self.reference_id = reference_id
        self.token = token
