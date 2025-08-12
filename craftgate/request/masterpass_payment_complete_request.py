from typing import Optional

class MasterpassPaymentCompleteRequest(object):
    def __init__(
        self,
        reference_id=None,  # type: Optional[str]
        token=None          # type: Optional[str]
    ):
        self.reference_id = reference_id
        self.token = token