from typing import List, Optional
from craftgate.model.refund_type import RefundType
from craftgate.model.currency import Currency
from craftgate.response.common.base_payment_refund_response import BasePaymentRefundResponse
from craftgate.response.payment_transaction_refund_response import PaymentTransactionRefundResponse


class PaymentRefundResponse(BasePaymentRefundResponse):
    def __init__(
        self,
        refund_type=None,  # type: Optional[RefundType]
        currency=None,  # type: Optional[Currency]
        payment_transaction_refunds=None,  # type: Optional[List[PaymentTransactionRefundResponse]]
        **kwargs
    ):
        super(PaymentRefundResponse, self).__init__(**kwargs)
        self.refund_type = refund_type
        self.currency = currency
        self.payment_transaction_refunds = payment_transaction_refunds