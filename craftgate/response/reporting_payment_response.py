from decimal import Decimal
from typing import List, Optional

from craftgate.model.payment_refund_status import PaymentRefundStatus
from craftgate.response.common.base_payment_response import BasePaymentResponse
from craftgate.response.member_response import MemberResponse
from craftgate.response.reporting_payment_refund_response import ReportingPaymentRefundResponse


class ReportingPaymentResponse(BasePaymentResponse):
    def __init__(
            self,
            retry_count: Optional[int] = None,
            refundable_price: Optional[Decimal] = None,
            refund_status: Optional[PaymentRefundStatus] = None,
            buyer_member: Optional[MemberResponse] = None,
            refunds: Optional[List[ReportingPaymentRefundResponse]] = None,
            **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.retry_count = retry_count
        self.refundable_price = refundable_price
        self.refund_status = refund_status
        self.buyer_member = buyer_member
        self.refunds = refunds
