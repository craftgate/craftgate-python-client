from typing import Optional
from craftgate.request.create_payment_request import CreatePaymentRequest

class InitThreeDSPaymentRequest(CreatePaymentRequest):
    def __init__(self, callback_url=None, **kwargs):
        # type: (Optional[str], ...) -> None
        super(InitThreeDSPaymentRequest, self).__init__(**kwargs)
        self.callback_url = callback_url