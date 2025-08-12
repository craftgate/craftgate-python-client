from typing import Optional
from datetime import datetime

from craftgate.model.settlement_type import SettlementType


class SearchPayoutCompletedTransactionsRequest(object):
    def __init__(
        self,
        settlement_file_id=None,  # type: Optional[int]
        settlement_type=None,     # type: Optional[SettlementType]
        start_date=None,          # type: Optional[datetime]
        end_date=None,            # type: Optional[datetime]
        page=None,                # type: Optional[int]
        size=None                 # type: Optional[int]
    ):
        self.settlement_file_id = settlement_file_id
        self.settlement_type = settlement_type
        self.start_date = start_date
        self.end_date = end_date
        self.page = page
        self.size = size
