# tests/test_bank_account_tracking_sample.py
import os
import unittest

from craftgate.adapter.bank_account_tracking_adapter import BankAccountTrackingAdapter
from craftgate.request.search_bank_account_tracking_records_request import SearchBankAccountTrackingRecordsRequest
from craftgate.request_options import RequestOptions


class BankAccountTrackingSample(unittest.TestCase):
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
        cls.craftgate = BankAccountTrackingAdapter(options)

    def test_search_bank_account_tracking_records(self):
        request = SearchBankAccountTrackingRecordsRequest(
            page=0,
            size=10,
            sender_iban="TR260006231316984553846956"
        )

        response = self.craftgate.search_records(request)
        print(vars(response))
        self.assertIsNotNone(response)

    def test_retrieve_bank_account_tracking_record(self):
        record_id = 158011
        response = self.craftgate.retrieve_record(record_id)
        print(vars(response))
        self.assertIsNotNone(response)
        self.assertEqual(response.id, record_id)


if __name__ == "__main__":
    unittest.main()
