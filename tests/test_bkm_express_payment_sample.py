# tests/test_bkm_express_payment_sample.py
import os
import unittest

from craftgate import Craftgate, RequestOptions
from craftgate.request.generate_bkm_express_token import BkmExpressGenerateTokenRequest


class BkmExpressPaymentSample(unittest.TestCase):
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
        cls.bkm_express_payment = Craftgate(options).bkm_express_payment()

    def test_generate_token(self):
        request = BkmExpressGenerateTokenRequest(
            gsm_number="5350000000",
            user_id="1234567890"
        )

        response = self.bkm_express_payment.generate_token(request)
        print(response)
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
