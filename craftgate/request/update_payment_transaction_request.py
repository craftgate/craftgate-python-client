from typing import Optional
from decimal import Decimal

class UpdatePaymentTransactionRequest(object):
    def __init__(
        self,
        payment_transaction_id=None,       # type: Optional[int]
        sub_merchant_member_id=None,       # type: Optional[int]
        sub_merchant_member_price=None     # type: Optional[Decimal]
    ):
        self.payment_transaction_id = payment_transaction_id
        self.sub_merchant_member_id = sub_merchant_member_id
        self.sub_merchant_member_price = sub_merchant_member_price