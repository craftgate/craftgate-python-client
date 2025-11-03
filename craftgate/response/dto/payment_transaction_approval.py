from typing import Optional

from craftgate.model.approval_status import ApprovalStatus


class PaymentTransactionApproval(object):
    def __init__(
            self,
            payment_transaction_id: Optional[int] = None,
            approval_status: Optional[ApprovalStatus] = None,
            failed_reason: Optional[str] = None
    ) -> None:
        if approval_status is not None and not isinstance(approval_status, ApprovalStatus):
            approval_status = ApprovalStatus(approval_status)

        self.payment_transaction_id = payment_transaction_id
        self.approval_status = approval_status
        self.failed_reason = failed_reason
