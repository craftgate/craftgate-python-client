from datetime import datetime
from typing import Optional

from craftgate.model.report_period import ReportPeriod
from craftgate.model.report_type import ReportType


class ReportDemandResponse:
    def __init__(
            self,
            id: Optional[int] = None,
            report_type: Optional[ReportType] = None,
            report_period: Optional[ReportPeriod] = None,
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None
    ) -> None:
        self.id = id
        self.report_type = report_type
        self.report_period = report_period
        self.start_date = start_date
        self.end_date = end_date
