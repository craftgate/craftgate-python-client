from decimal import Decimal
from typing import Optional


class UpdatePaymentTransactionRequest(object):
    def __init__(
            self,
            payment_transaction_id: Optional[int] = None,
            sub_merchant_member_id: Optional[int] = None,
            sub_merchant_member_price: Optional[Decimal] = None
    ) -> None:
        self.payment_transaction_id = payment_transaction_id
        self.sub_merchant_member_id = sub_merchant_member_id
        self.sub_merchant_member_price = sub_merchant_member_price
