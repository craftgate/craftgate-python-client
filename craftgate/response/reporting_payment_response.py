from typing import Optional, List
from decimal import Decimal

from craftgate.model.payment_refund_status import PaymentRefundStatus
from craftgate.response.common.base_payment_response import BasePaymentResponse
from craftgate.response.member_response import MemberResponse
from craftgate.response.reporting_payment_refund_response import ReportingPaymentRefundResponse


class ReportingPaymentResponse(BasePaymentResponse):
    def __init__(
        self,
        retry_count=None,          # type: Optional[int]
        refundable_price=None,     # type: Optional[Decimal]
        refund_status=None,        # type: Optional[PaymentRefundStatus]
        buyer_member=None,         # type: Optional[MemberResponse]
        refunds=None,               # type: Optional[List[ReportingPaymentRefundResponse]]
        **kwargs
    ):
        super(ReportingPaymentResponse, self).__init__(**kwargs)
        self.retry_count = retry_count
        self.refundable_price = refundable_price
        self.refund_status = refund_status
        self.buyer_member = buyer_member
        self.refunds = refunds or []