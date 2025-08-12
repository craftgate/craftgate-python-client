from craftgate.response.common.base_payment_refund_response import BasePaymentRefundResponse
from craftgate.model.payment_type import PaymentType
from craftgate.response.dto.payment_error import PaymentError


class ReportingPaymentRefundResponse(BasePaymentRefundResponse):
    def __init__(
        self,
        payment_type=None,  # type: PaymentType
        error=None,         # type: PaymentError
        **kwargs
    ):
        super(ReportingPaymentRefundResponse, self).__init__(**kwargs)
        self.payment_type = payment_type
        self.error = error