import unittest
from unittest.mock import MagicMock

from craftgate import RequestOptions
from craftgate.adapter.file_reporting_adapter import FileReportingAdapter
from craftgate.model import ReportFileType
from craftgate.request import RetrieveReportRequest


class DownloadReportTest(unittest.TestCase):

    def setUp(self):
        options = RequestOptions(api_key="api-key", secret_key="secret-key", base_url="https://sandbox-api.craftgate.io")
        self.adapter = FileReportingAdapter(options)
        self.adapter._http_client = MagicMock()
        self.adapter._http_client.request.return_value = b"file-bytes"

    def test_should_call_download_path_with_file_type(self):
        result = self.adapter.download_report(
            RetrieveReportRequest(file_type=ReportFileType.XLSX), report_id=42)

        self.assertEqual(b"file-bytes", result)
        kwargs = self.adapter._http_client.request.call_args.kwargs
        self.assertEqual("GET", kwargs["method"])
        self.assertEqual("https://sandbox-api.craftgate.io/file-reporting/v1/reports/42/download?fileType=XLSX", kwargs["url"])
        self.assertIsNone(kwargs["body"])
        self.assertIs(bytes, kwargs["response_type"])
        self.assertEqual("application/octet-stream", kwargs["headers"]["Content-Type"])

    def test_should_not_use_legacy_retrieve_path(self):
        self.adapter.download_report(
            RetrieveReportRequest(file_type=ReportFileType.CSV), report_id=7)

        url = self.adapter._http_client.request.call_args.kwargs["url"]
        self.assertTrue(url.endswith("/reports/7/download?fileType=CSV"))
