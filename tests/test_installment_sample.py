# tests/test_installment_sample.py
import os
import unittest

from craftgate.adapter.installment_adapter import InstallmentAdapter
from craftgate.model.currency import Currency
from craftgate.request.search_installments_request import SearchInstallmentsRequest
from craftgate.request_options import RequestOptions


class InstallmentSample(unittest.TestCase):
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
        cls.craftgate = InstallmentAdapter(options)

    def test_search_installments(self):
        request = SearchInstallmentsRequest(
            bin_number="520922",
            price=100,
            currency=Currency.TRY
        )

        resp = self.craftgate.search_installments(request)

        print(vars(resp))
        self.assertIsNotNone(resp)
        self.assertIsInstance(getattr(resp, "items", []), list)

    def test_retrieve_bin_number(self):
        bin_number = "525864"
        resp = self.craftgate.retrieve_bin_number(bin_number)

        print(vars(resp))
        self.assertIsNotNone(resp)
        self.assertEqual(getattr(resp, "bin_number", None), bin_number)


if __name__ == "__main__":
    unittest.main()
