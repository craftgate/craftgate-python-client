# tests/test_juzdan_payment_sample.py
import os
import unittest
import uuid
from decimal import Decimal

from craftgate import Craftgate, RequestOptions
from craftgate.model import Currency, PaymentGroup, PaymentPhase, PaymentSource, PaymentType
from craftgate.request import InitJuzdanPaymentRequest
from craftgate.request.dto import PaymentItem


class JuzdanSample(unittest.TestCase):
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
        cls.juzdan_payment = Craftgate(options).juzdan_payment()

    def test_init(self):
        items = [
            PaymentItem(price=Decimal("1"), name="test123", external_id=str(uuid.uuid4()))
        ]
        req = InitJuzdanPaymentRequest(
            price=Decimal("1"),
            paid_price=Decimal("1"),
            currency=Currency.TRY,
            payment_group=PaymentGroup.PRODUCT,
            conversation_id="testConversationId",
            external_id="testExternalId",
            callback_url="www.testCallbackUrl.com",
            client_type=InitJuzdanPaymentRequest.ClientType.W,
            items=items,
            payment_phase=PaymentPhase.AUTH,
            payment_channel="testPaymentChannel",
            bank_order_id="testBankOrderId"
        )
        resp = self.juzdan_payment.init(req)
        print(resp)

        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp.juzdan_qr_url)
        self.assertIsNotNone(resp.reference_id)

    def test_retrieve(self):
        reference_id = "5493c7a7-4d8b-4517-887d-f8b8f826a3d0"
        resp = self.juzdan_payment.retrieve(reference_id)
        print(resp)

        self.assertIsNotNone(resp)
        self.assertEqual(PaymentSource.JUZDAN, resp.payment_source)
        self.assertEqual(PaymentType.CARD_PAYMENT, resp.payment_type)


if __name__ == "__main__":
    unittest.main()
