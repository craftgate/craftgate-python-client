# tests/test_file_reporting_sample.py
import os
import unittest
from datetime import date

from craftgate import Craftgate, RequestOptions
from craftgate.model import ReportFileType
from craftgate.request import RetrieveDailyPaymentReportRequest, RetrieveDailyTransactionReportRequest


class FileReportingSample(unittest.TestCase):
    API_KEY = os.environ.get("CG_API_KEY", "YOUR_API_KEY")
    SECRET_KEY = os.environ.get("CG_SECRET_KEY", "YOUR_SECRET_KEY")
    BASE_URL = os.environ.get("CG_BASE_URL", "https://sandbox-api.craftgate.io")

    @classmethod
    def setUpClass(cls):
        opts = RequestOptions(api_key=cls.API_KEY, secret_key=cls.SECRET_KEY, base_url=cls.BASE_URL)
        cls.file_reporting = Craftgate(opts).file_reporting()

    def test_retrieve_daily_transaction_report_csv(self):
        request = RetrieveDailyTransactionReportRequest(
            report_date=date(2025, 8, 8),
            file_type=ReportFileType.CSV
        )

        blob = self.file_reporting.retrieve_daily_transaction_report(request)

        print(blob.decode('utf-8', errors='replace')[:200])
        self.assertIsInstance(blob, (bytes, bytearray))
        self.assertGreater(len(blob), 0)

        file_name = f"transaction-report-{request.report_date.isoformat()}.{request.file_type.value}"
        out_path = os.path.join(os.getcwd(), file_name)

        with open(out_path, "wb") as f:
            f.write(blob)

    def test_retrieve_daily_payment_report_csv(self):
        request = RetrieveDailyPaymentReportRequest(
            report_date=date(2025, 8, 7),
            file_type=ReportFileType.CSV
        )

        blob = self.file_reporting.retrieve_daily_payment_report(request)

        print(blob.decode('utf-8', errors='replace')[:200])
        self.assertIsInstance(blob, (bytes, bytearray))
        self.assertGreater(len(blob), 0)

        file_name = f"payment-report-{request.report_date.isoformat()}.{request.file_type.value}"
        out_path = os.path.join(os.getcwd(), file_name)

        with open(out_path, "wb") as f:
            f.write(blob)


if __name__ == "__main__":
    unittest.main()
