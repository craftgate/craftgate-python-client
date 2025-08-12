from datetime import datetime
from typing import Optional

from craftgate.model.file_status import FileStatus


class SearchPayoutRowsRequest(object):
    def __init__(
            self,
            page: int = 0,
            size: int = 10,
            file_status: Optional[FileStatus] = None,
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None
    ) -> None:
        self.page = page
        self.size = size
        self.file_status = file_status
        self.start_date = start_date
        self.end_date = end_date
