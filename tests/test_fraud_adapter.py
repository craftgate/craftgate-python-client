# tests/test_fraud_adapter.py
import os
import unittest
from datetime import datetime, timedelta
from craftgate import Craftgate

from craftgate.model import FraudAction, FraudValueType, FraudCheckStatus
from craftgate.request import FraudValueListRequest, SearchFraudChecksRequest
from craftgate.request_options import RequestOptions
from craftgate.utils.converter import Converter


class FraudAdapterSample(unittest.TestCase):
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
        cls.fraud = Craftgate(options).fraud()

    def test_create_value_list(self):
        self.fraud.create_value_list("mailList", FraudValueType.EMAIL)

    def test_add_value_to_value_list(self):
        req = FraudValueListRequest(
            list_name="test",
            type=FraudValueType.IP,
            label="local ip 2",
            value="127.0.0.2",
            duration_in_seconds=600
        )
        self.fraud.add_value_to_value_list(req)

    def test_retrieve_value_list(self):
        resp = self.fraud.retrieve_value_list("test")
        print(Converter.to_clean_dict(resp))

        self.assertIsNotNone(resp)
        self.assertEqual("test", resp.name)

    def test_retrieve_all_value_lists(self):
        resp = self.fraud.retrieve_all_value_lists()
        print(Converter.to_clean_dict(resp))

        self.assertIsNotNone(resp)
        self.assertTrue(resp.items)

    def test_remove_value_from_value_list(self):
        self.fraud.remove_value_from_value_list(list_name="test", value_id="e9bca836-6933-4ca1-a323-cb7e02ae4981")

    def test_delete_value_list(self):
        self.fraud.delete_value_list("ipList")

    def test_search_fraud_checks(self):
        now = datetime.now()
        req = SearchFraudChecksRequest(
            min_created_date=now - timedelta(days=2),
            max_created_date=now,
            action=FraudAction.REVIEW,
            check_status=FraudCheckStatus.WAITING
        )
        resp = self.fraud.search_fraud_checks(req)
        print(Converter.to_clean_dict(resp))

        self.assertIsNotNone(resp)
        self.assertTrue(resp.items)

    def test_update_fraud_check_status(self):
        self.fraud.update_fraud_check_status(int(2613), FraudCheckStatus.FRAUD)


if __name__ == "__main__":
    unittest.main()
