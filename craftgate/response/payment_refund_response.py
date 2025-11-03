from typing import List, Optional

from craftgate.model.currency import Currency
from craftgate.model.refund_type import RefundType
from craftgate.response.common.base_payment_refund_response import BasePaymentRefundResponse
from craftgate.response.payment_transaction_refund_response import PaymentTransactionRefundResponse


class PaymentRefundResponse(BasePaymentRefundResponse):
    def __init__(
            self,
            refund_type: Optional[RefundType] = None,
            currency: Optional[Currency] = None,
            payment_transaction_refunds: Optional[List[PaymentTransactionRefundResponse]] = None,
            **kwargs
    ) -> None:
        super(PaymentRefundResponse, self).__init__(**kwargs)
        self.refund_type = refund_type
        self.currency = currency
        self.payment_transaction_refunds = payment_transaction_refunds
