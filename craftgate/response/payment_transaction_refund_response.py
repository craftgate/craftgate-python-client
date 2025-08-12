from craftgate.model.currency import Currency
from craftgate.response.common.base_payment_transaction_refund_response import BasePaymentTransactionRefundResponse


class PaymentTransactionRefundResponse(BasePaymentTransactionRefundResponse):
    def __init__(self, currency=None, payment_id=None, **kwargs):
        super(PaymentTransactionRefundResponse, self).__init__(**kwargs)
        self.currency = Currency(currency) if currency else None
        self.payment_id = payment_id