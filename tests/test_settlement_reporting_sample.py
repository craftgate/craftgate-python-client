# tests/test_settlement_reporting_sample.py
import os
import unittest
from datetime import datetime, timedelta

from craftgate import Craftgate, RequestOptions
from craftgate.model import FileStatus, SettlementType
from craftgate.request import SearchPaymentTransactionPayoutsRequest, SearchPayoutBouncedTransactionsRequest, \
    SearchPayoutCompletedItemsRequest, SearchPayoutRowsRequest


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
        cls.settlement_reporting = Craftgate(options).settlement_reporting()

    def test_search_settlement_payout_completed_transactions(self):
        now = datetime.now()
        start = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        end = (now - timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=0)
        request = SearchPayoutCompletedItemsRequest(
            settlement_type=SettlementType.SETTLEMENT,
            start_date=start,
            end_date=end,
            page=0,
            size=10
        )
        response = self.settlement_reporting.search_payout_completed_items(request)
        print(response)
        self.assertTrue(len(response.items) > 0)

    def test_search_bounced_settlement_payout_completed_transactions(self):
        now = datetime.now()
        start = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        end = (now - timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=0)
        request = SearchPayoutCompletedItemsRequest(
            settlement_type=SettlementType.BOUNCED_SETTLEMENT,
            start_date=start,
            end_date=end,
            page=0,
            size=10
        )
        response = self.settlement_reporting.search_payout_completed_items(request)
        print(response)
        self.assertTrue(len(response.items) > 0)

    def test_search_payout_bounced_transactions(self):
        now = datetime.now()
        start = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        end = (now - timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=0)
        request = SearchPayoutBouncedTransactionsRequest(
            start_date=start,
            end_date=end
        )
        response = self.settlement_reporting.search_bounced_payout_transactions(request)
        print(response)
        self.assertTrue(len(response.items) > 0)

    def test_retrieve_settlement_row(self):
        settlement_row_id = 1
        response = self.settlement_reporting.retrieve_settlement_row(settlement_row_id)
        print(response)
        self.assertIsNotNone(response)
        self.assertTrue(len(response.items) > 0)

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
        response = self.settlement_reporting.search_payout_rows(request)
        print(response)
        self.assertTrue(len(response.items) > 0)

    def test_retrieve_payment_transaction_payout(self):
        payment_transaction_id = 1
        response = self.settlement_reporting.retrieve_payment_transaction_payout(payment_transaction_id)
        print(response)
        self.assertEqual(payment_transaction_id, response.payment_transaction_id)
        self.assertTrue(len(response.payout_items) > 0)

    def test_search_payment_transaction_payouts(self):
        request = SearchPaymentTransactionPayoutsRequest(
            payment_transaction_ids=[1, 2]
        )
        response = self.settlement_reporting.search_payment_transaction_payouts(request)
        print(response)
        self.assertTrue(len(response.items) > 0)


if __name__ == "__main__":
    unittest.main()
