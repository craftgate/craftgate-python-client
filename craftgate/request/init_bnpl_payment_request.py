from typing import Optional, List
from craftgate.request.init_apm_payment_request import InitApmPaymentRequest
from craftgate.request.dto.bnpl_payment_cart_item import BnplPaymentCartItem

class InitBnplPaymentRequest(InitApmPaymentRequest):
    def __init__(self,
                 bank_code=None,                 # type: Optional[str]
                 cart_items=None,                # type: Optional[List[BnplPaymentCartItem]]
                 **kwargs):
        super(InitBnplPaymentRequest, self).__init__(**kwargs)
        self.bank_code = bank_code
        self.cart_items = cart_items