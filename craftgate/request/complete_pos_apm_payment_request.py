from typing import Optional, Dict, Any


class CompletePosApmPaymentRequest(object):
    def __init__(self,
                 payment_id=None,  # type: Optional[int]
                 additional_params=None  # type: Optional[Dict[str, Any]]
                 ):
        self.payment_id = payment_id
        self.additional_params = additional_params
