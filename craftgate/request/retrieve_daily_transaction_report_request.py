from datetime import date
from typing import Optional
from urllib.parse import urlencode


class RetrieveDailyTransactionReportRequest:
    def __init__(self, report_date: Optional[date] = None, file_type: Optional[str] = None):
        self.report_date = report_date
        self.file_type = file_type