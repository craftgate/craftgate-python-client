# tests/test_payment_token_sample.py
import os
import unittest

from craftgate.adapter.payment_token_adapter import PaymentTokenAdapter
from craftgate.request.create_payment_token_request import CreatePaymentTokenRequest
from craftgate.request_options import RequestOptions

try:
    from craftgate.model.apm_type import ApmType
except Exception:
    ApmType = None


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
        cls.adapter = PaymentTokenAdapter(options)

    def test_create_payment_token(self):
        request = CreatePaymentTokenRequest(
            value="value-to-be-tokenized",
            issuer="EDENRED"
        )
        response = self.adapter.create_payment_token(request)
        print(vars(response))
        self.assertIsNotNone(response)
        if ApmType is not None and hasattr(ApmType, "EDENRED"):
            self.assertEqual(response.issuer, ApmType.EDENRED)
        else:
            self.assertEqual(str(response.issuer), "EDENRED")
        self.assertIsNotNone(response.token)

    def test_delete_payment_token(self):
        token = "token-to-be-deleted"
        self.adapter.delete_payment_token(token)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
