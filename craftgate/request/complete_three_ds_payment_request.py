from typing import Optional


class CompleteThreeDSPaymentRequest(object):
    def __init__(self,
                 payment_id=None  # type: Optional[int]
                 ):
        self.payment_id = payment_id
