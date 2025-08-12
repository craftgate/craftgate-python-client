from typing import Optional
from datetime import datetime
from craftgate.model.file_status import FileStatus


class SearchPayoutRowsRequest(object):
    def __init__(
        self,
        page=0,               # type: Optional[int]
        size=10,              # type: Optional[int]
        file_status=None,     # type: Optional[FileStatus]
        start_date=None,      # type: Optional[datetime]
        end_date=None         # type: Optional[datetime]
    ):
        self.page = page
        self.size = size
        self.file_status = file_status
        self.start_date = start_date
        self.end_date = end_date
