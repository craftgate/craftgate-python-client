from craftgate.model.approval_status import ApprovalStatus

class PaymentTransactionApproval(object):
    def __init__(self, payment_transaction_id=None, approval_status=None, failed_reason=None):
        self.payment_transaction_id = payment_transaction_id
        self.approval_status = ApprovalStatus(approval_status) if approval_status else None
        self.failed_reason = failed_reason