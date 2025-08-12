from typing import List, Optional

from craftgate.response.dto.payout_completed_transaction import PayoutCompletedTransaction


class PayoutCompletedTransactionListResponse(object):
    def __init__(
            self,
            items: Optional[List[PayoutCompletedTransaction]] = None,
            page: Optional[int] = None,
            size: Optional[int] = None,
            total_size: Optional[int] = None
    ) -> None:
        self.items = items
        self.page = page
        self.size = size
        self.total_size = total_size
