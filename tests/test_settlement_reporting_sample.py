# tests/test_settlement_reporting_sample.py
import os
import unittest
from datetime import datetime, timedelta

from craftgate.adapter.settlement_reporting_adapter import SettlementReportingAdapter
from craftgate.model.file_status import FileStatus
from craftgate.model.settlement_type import SettlementType
from craftgate.request.search_payout_bounced_transactions_request import SearchPayoutBouncedTransactionsRequest
from craftgate.request.search_payout_completed_transactions_request import SearchPayoutCompletedTransactionsRequest
from craftgate.request.search_payout_rows_request import SearchPayoutRowsRequest
from craftgate.request_options import RequestOptions


class SettlementReportingSample(unittest.TestCase):
    API_KEY = os.environ.get("CG_API_KEY", "YOUR_API_KEY")
    SECRET_KEY = os.environ.get("CG_SECRET_KEY", "YOUR_SECRET_KEY")
    BASE_URL = os.environ.get("CG_BASE_URL", "https://sandbox-api.craftgate.io")

    @classmethod
    def setUpClass(cls):
        options = RequestOptions(
            api_key=cls.API_KEY,
            secret_key=cls.SECRET_KEY,
            base_url=cls.BASE_URL
        )
        cls.adapter = SettlementReportingAdapter(options)

    def test_search_settlement_payout_completed_transactions(self):
        now = datetime.now()
        start = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        end = (now - timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=0)
        request = SearchPayoutCompletedTransactionsRequest(
            settlement_type=SettlementType.SETTLEMENT,
            start_date=start,
            end_date=end,
            page=0,
            size=10
        )
        response = self.adapter.search_payout_completed_transactions(request)
        print(vars(response))
        self.assertTrue(len(response.items) > 0)

    def test_search_bounced_settlement_payout_completed_transactions(self):
        now = datetime.now()
        start = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        end = (now - timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=0)
        request = SearchPayoutCompletedTransactionsRequest(
            settlement_type=SettlementType.BOUNCED_SETTLEMENT,
            start_date=start,
            end_date=end,
            page=0,
            size=10
        )
        response = self.adapter.search_payout_completed_transactions(request)
        print(vars(response))
        self.assertTrue(len(response.items) > 0)

    def test_search_payout_bounced_transactions(self):
        now = datetime.now()
        start = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        end = (now - timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=0)
        request = SearchPayoutBouncedTransactionsRequest(
            start_date=start,
            end_date=end
        )
        response = self.adapter.search_bounced_payout_transactions(request)
        print(vars(response))
        self.assertTrue(len(response.items) > 0)

    def test_retrieve_payout_details(self):
        payout_id = 1
        response = self.adapter.retrieve_payout_details(payout_id)
        print(vars(response))
        self.assertIsNotNone(response)

    def test_search_payout_rows(self):
        now = datetime.now()
        start = now - timedelta(days=10)
        end = now
        request = SearchPayoutRowsRequest(
            file_status=FileStatus.CREATED,
            start_date=start,
            end_date=end,
            page=0,
            size=10
        )
        response = self.adapter.search_payout_rows(request)
        print(vars(response))
        self.assertTrue(len(response.items) > 0)


if __name__ == "__main__":
    unittest.main()
