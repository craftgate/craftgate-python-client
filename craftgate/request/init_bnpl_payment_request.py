from typing import List, Optional

from craftgate.request.dto.bnpl_payment_cart_item import BnplPaymentCartItem
from craftgate.request.init_apm_payment_request import InitApmPaymentRequest


class InitBnplPaymentRequest(InitApmPaymentRequest):
    def __init__(
        self,
        bank_code: Optional[str] = None,
        cart_items: Optional[List[BnplPaymentCartItem]] = None,
        **kwargs
    ) -> None:
        super(InitBnplPaymentRequest, self).__init__(**kwargs)
        self.bank_code = bank_code
        self.cart_items = cart_items
