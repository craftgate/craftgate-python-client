# tests/test_merchant_apm_sample.py
import os
import unittest

from craftgate.adapter.merchant_apm_adapter import MerchantApmAdapter
from craftgate.request_options import RequestOptions


class MerchantApmSample(unittest.TestCase):
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
        cls.adapter = MerchantApmAdapter(options)

    def test_retrieve_merchant_apms(self):
        response = self.adapter.retrieve_apms()
        print(vars(response))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
