from typing import List, Optional

from craftgate.model.report_file_type import ReportFileType
from craftgate.request.common.base_request import BaseRequest
from craftgate.request.dto.report_filter import ReportFilter


class CreateReportFromTemplateRequest(BaseRequest):
    def __init__(
            self,
            filters: Optional[List[ReportFilter]] = None,
            file_formats: Optional[List[ReportFileType]] = None
    ) -> None:
        self.filters = filters
        self.file_formats = file_formats
