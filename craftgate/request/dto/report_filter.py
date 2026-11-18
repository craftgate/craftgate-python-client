from datetime import datetime
from typing import Any, List, Optional


class ReportFilter(object):
    REPORT_DATE_FILTER_NAME = "reportDate"

    def __init__(
            self,
            name: Optional[str] = None,
            values: Optional[List[Any]] = None
    ) -> None:
        self.name = name
        self.values = values

    @staticmethod
    def report_date(start_date: datetime, end_date: datetime) -> "ReportFilter":
        return ReportFilter(ReportFilter.REPORT_DATE_FILTER_NAME, [start_date, end_date])
