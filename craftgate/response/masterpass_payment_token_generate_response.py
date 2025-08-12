from typing import Optional

class MasterpassPaymentTokenGenerateResponse(object):
    def __init__(
        self,
        token=None,          # type: Optional[str]
        reference_id=None,   # type: Optional[str]
        order_no=None        # type: Optional[str]
    ):
        self.token = token
        self.reference_id = reference_id
        self.order_no = order_no