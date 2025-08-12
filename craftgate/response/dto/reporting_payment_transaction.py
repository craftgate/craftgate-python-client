from datetime import datetime

from craftgate.model.payment_refund_status import PaymentRefundStatus
from craftgate.response.dto.payout_status import PayoutStatus
from craftgate.response.dto.payment_transaction import PaymentTransaction


class ReportingPaymentTransaction(PaymentTransaction):
    def __init__(
        self,
        created_date=None,                 # type: datetime
        transaction_status_date=None,      # type: datetime
        refundable_price=None,             # type: float
        sub_merchant_member=None,          # type: object  # MemberResponse
        refund_status=None,                # type: PaymentRefundStatus
        payout_status=None,                # type: PayoutStatus
        bank_commission_rate=None,         # type: float
        bank_commission_rate_amount=None,  # type: float
        **kwargs
    ):
        super(ReportingPaymentTransaction, self).__init__(**kwargs)
        self.created_date = created_date
        self.transaction_status_date = transaction_status_date
        self.refundable_price = refundable_price
        self.sub_merchant_member = sub_merchant_member
        self.refund_status = refund_status
        self.payout_status = payout_status
        self.bank_commission_rate = bank_commission_rate
        self.bank_commission_rate_amount = bank_commission_rate_amount