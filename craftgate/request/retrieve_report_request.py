from typing import Optional

from craftgate.model.report_file_type import ReportFileType


class RetrieveReportRequest:
    def __init__(self, file_type: Optional[ReportFileType] = None) -> None:
        self.file_type = file_type
