from typing import Optional, Dict


class CompleteApmPaymentRequest(object):
    def __init__(self,
                 payment_id=None,  # type: Optional[int]
                 additional_params=None  # type: Optional[Dict[str, str]]
                 ):
        self.payment_id = payment_id
        self.additional_params = additional_params
