from datetime import datetime
from typing import Optional

from craftgate.model.settlement_type import SettlementType


class SearchPayoutCompletedTransactionsRequest(object):
    def __init__(
            self,
            settlement_file_id: Optional[int] = None,
            settlement_type: Optional[SettlementType] = None,
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None,
            page: Optional[int] = None,
            size: Optional[int] = None
    ) -> None:
        self.settlement_file_id = settlement_file_id
        self.settlement_type = settlement_type
        self.start_date = start_date
        self.end_date = end_date
        self.page = page
        self.size = size
