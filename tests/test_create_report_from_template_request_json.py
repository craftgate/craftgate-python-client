import json
import unittest
from datetime import datetime

from craftgate.model import ReportFileType, ReportState
from craftgate.request import CreateReportFromTemplateRequest
from craftgate.request.dto import ReportFilter
from craftgate.response import ReportFromTemplateResponse
from craftgate.utils.converter import Converter
from craftgate.utils.serializer import serialize_request_body

START_DATE = datetime(2025, 11, 19, 9, 15, 31, 622824)
END_DATE = datetime(2025, 11, 27, 9, 15, 31, 622843)
REPORT_DATE = {"name": "reportDate", "values": ["2025-11-19T09:15:31.622824", "2025-11-27T09:15:31.622843"]}


class CreateReportFromTemplateRequestJsonTest(unittest.TestCase):

    def test_should_serialize_report_date_filter_and_file_format(self):
        request = CreateReportFromTemplateRequest(
            filters=[ReportFilter.report_date(START_DATE, END_DATE)],
            file_formats=[ReportFileType.XLSX]
        )

        body = json.loads(serialize_request_body(request))

        self.assertEqual({"filters": [REPORT_DATE], "fileFormats": ["XLSX"]}, body)

    def test_should_omit_file_formats_when_not_set(self):
        request = CreateReportFromTemplateRequest(filters=[ReportFilter.report_date(START_DATE, END_DATE)])

        body = json.loads(serialize_request_body(request))

        self.assertEqual({"filters": [REPORT_DATE]}, body)

    def test_should_keep_filters_in_insertion_order(self):
        request = CreateReportFromTemplateRequest(
            filters=[
                ReportFilter(name="status", values=["SUCCESS"]),
                ReportFilter.report_date(START_DATE, END_DATE)
            ],
            file_formats=[ReportFileType.CSV]
        )

        body = json.loads(serialize_request_body(request))

        self.assertEqual(
            {"filters": [{"name": "status", "values": ["SUCCESS"]}, REPORT_DATE], "fileFormats": ["CSV"]},
            body)

    def test_should_map_response(self):
        data = {"id": 5, "reportState": "DEMANDED", "columns": ["a"], "reportSchemaId": 9,
                "filters": [{"name": "status", "values": ["SUCCESS"]}]}

        response = Converter.auto_map(ReportFromTemplateResponse, data)

        self.assertEqual(5, response.id)
        self.assertEqual(ReportState.DEMANDED, response.report_state)
        self.assertEqual(9, response.report_schema_id)
        self.assertIsInstance(response.filters[0], ReportFilter)
        self.assertEqual("status", response.filters[0].name)


if __name__ == "__main__":
    unittest.main()
