from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.payment_refund_status import PaymentRefundStatus
from craftgate.response.dto.payment_transaction import PaymentTransaction
from craftgate.response.dto.payout_status import PayoutStatus
from craftgate.response.member_response import MemberResponse


class ReportingPaymentTransaction(PaymentTransaction):
    def __init__(
            self,
            created_date: Optional[datetime] = None,
            transaction_status_date: Optional[datetime] = None,
            refundable_price: Optional[Decimal] = None,
            sub_merchant_member: Optional[MemberResponse] = None,
            refund_status: Optional[PaymentRefundStatus] = None,
            payout_status: Optional[PayoutStatus] = None,
            bank_commission_rate: Optional[Decimal] = None,
            bank_commission_rate_amount: Optional[Decimal] = None,
            **kwargs
    ) -> None:
        super(ReportingPaymentTransaction, self).__init__(**kwargs)
        self.created_date = created_date
        self.transaction_status_date = transaction_status_date
        self.refundable_price = refundable_price
        self.sub_merchant_member = sub_merchant_member
        self.refund_status = refund_status
        self.payout_status = payout_status
        self.bank_commission_rate = bank_commission_rate
        self.bank_commission_rate_amount = bank_commission_rate_amount
