from typing import List, Optional

from craftgate.model.report_state import ReportState
from craftgate.request.dto.report_filter import ReportFilter


class ReportFromTemplateResponse:
    def __init__(
            self,
            id: Optional[int] = None,
            report_state: Optional[ReportState] = None,
            filters: Optional[List[ReportFilter]] = None,
            columns: Optional[List[str]] = None,
            report_schema_id: Optional[int] = None
    ) -> None:
        self.id = id
        self.report_state = report_state
        self.filters = filters
        self.columns = columns
        self.report_schema_id = report_schema_id
