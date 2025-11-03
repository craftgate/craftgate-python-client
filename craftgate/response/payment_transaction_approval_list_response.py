from craftgate.response.common.list_response import ListResponse
from craftgate.response.dto.payment_transaction_approval import PaymentTransactionApproval


class PaymentTransactionApprovalListResponse(ListResponse[PaymentTransactionApproval]):
    item_type = PaymentTransactionApproval
