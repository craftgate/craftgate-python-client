from typing import Optional

from craftgate.model.currency import Currency
from craftgate.response.common.base_payment_transaction_refund_response import BasePaymentTransactionRefundResponse


class PaymentTransactionRefundResponse(BasePaymentTransactionRefundResponse):
    def __init__(
            self,
            currency: Optional[Currency] = None,
            payment_id: Optional[int] = None,
            **kwargs
    ) -> None:
        super(PaymentTransactionRefundResponse, self).__init__(**kwargs)
        self.currency = currency
        self.payment_id = payment_id
