from datetime import datetime
from typing import Optional


class SearchPayoutBouncedTransactionsRequest(object):
    def __init__(
            self,
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None
    ) -> None:
        self.start_date = start_date
        self.end_date = end_date
