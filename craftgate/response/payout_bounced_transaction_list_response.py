from craftgate.response.common.list_response import ListResponse
from craftgate.response.dto.payout_bounced_transaction import PayoutBouncedTransaction


class PayoutBouncedTransactionListResponse(ListResponse[PayoutBouncedTransaction]):
    item_type = PayoutBouncedTransaction
