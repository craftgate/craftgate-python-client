from typing import Optional
from craftgate.response.dto.payout_completed_transaction import PayoutCompletedTransaction


class PayoutCompletedTransactionListResponse(object):
    def __init__(
        self,
        items=None,       # type: Optional[list]
        page=None,        # type: Optional[int]
        size=None,        # type: Optional[int]
        total_size=None   # type: Optional[int]
    ):
        self.items = items or []  # type: list[PayoutCompletedTransaction]
        self.page = page
        self.size = size
        self.total_size = total_size
