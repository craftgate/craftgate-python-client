from typing import Optional
from datetime import datetime


class SearchPayoutBouncedTransactionsRequest(object):
    def __init__(
        self,
        start_date=None,  # type: Optional[datetime]
        end_date=None     # type: Optional[datetime]
    ):
        self.start_date = start_date
        self.end_date = end_date
