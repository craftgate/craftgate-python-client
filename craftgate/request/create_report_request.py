from datetime import datetime
from typing import Optional

from craftgate.model.report_period import ReportPeriod
from craftgate.model.report_type import ReportType


class CreateReportRequest:
    def __init__(
            self,
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None,
            report_type: ReportType = ReportType.TRANSACTION,
            report_period: ReportPeriod = ReportPeriod.INSTANT
    ) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.report_type = report_type
        self.report_period = report_period
