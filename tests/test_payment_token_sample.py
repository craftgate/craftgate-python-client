# tests/test_payment_token_sample.py
import os
import unittest

from craftgate import Craftgate, RequestOptions
from craftgate.model import ApmType
from craftgate.request import CreatePaymentTokenRequest


class PaymentTokenSample(unittest.TestCase):
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
        cls.payment_token = Craftgate(options).payment_token()

    def test_create_payment_token(self):
        request = CreatePaymentTokenRequest(
            value="value-to-be-tokenized",
            issuer="EDENRED"
        )
        response = self.payment_token.create_payment_token(request)
        print(response)
        self.assertIsNotNone(response)
        if ApmType is not None and hasattr(ApmType, "EDENRED"):
            self.assertEqual(response.issuer, ApmType.EDENRED)
        else:
            self.assertEqual(str(response.issuer), "EDENRED")
        self.assertIsNotNone(response.token)

    def test_delete_payment_token(self):
        token = "token-to-be-deleted"
        self.payment_token.delete_payment_token(token)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
