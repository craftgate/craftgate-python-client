# tests/test_bank_account_tracking_sample.py
import os
import unittest

from craftgate import Craftgate, RequestOptions
from craftgate.request import SearchBankAccountTrackingRecordsRequest


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
        cls.bank_account_tracking = Craftgate(options).bank_account_tracking()

    def test_search_bank_account_tracking_records(self):
        request = SearchBankAccountTrackingRecordsRequest(
            page=0,
            size=10,
            sender_iban="TR260006231316984553846956"
        )

        response = self.bank_account_tracking.search_records(request)
        print(vars(response))
        self.assertIsNotNone(response)

    def test_retrieve_bank_account_tracking_record(self):
        record_id = 158011
        response = self.bank_account_tracking.retrieve_record(record_id)
        print(vars(response))
        self.assertIsNotNone(response)
        self.assertEqual(response.id, record_id)


if __name__ == "__main__":
    unittest.main()
