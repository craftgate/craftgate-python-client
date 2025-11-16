from typing import Optional

from craftgate.model.approval_status import ApprovalStatus


class PaymentTransactionApproval(object):
    def __init__(
            self,
            payment_transaction_id: Optional[int] = None,
            approval_status: Optional[ApprovalStatus] = None,
            failed_reason: Optional[str] = None
    ) -> None:
        self.payment_transaction_id = payment_transaction_id
        self.approval_status = approval_status
        self.failed_reason = failed_reason
