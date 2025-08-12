from typing import Optional

class MasterpassPaymentThreeDSInitResponse(object):
    def __init__(
        self,
        payment_id=None,   # type: Optional[int]
        return_url=None    # type: Optional[str]
    ):
        self.payment_id = payment_id
        self.return_url = return_url