from typing import Optional

from craftgate.model.report_file_type import ReportFileType
from craftgate.request.common.base_request import BaseRequest


class RetrieveReportRequest(BaseRequest):
    def __init__(self, file_type: Optional[ReportFileType] = None) -> None:
        self.file_type = file_type
