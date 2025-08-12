from datetime import date
from typing import Optional

from craftgate.model.report_file_type import ReportFileType


class RetrieveDailyPaymentReportRequest(object):
    def __init__(
            self,
            report_date: Optional[date] = None,
            file_type: Optional[ReportFileType] = None
    ) -> None:
        self.report_date = report_date
        self.file_type = file_type
