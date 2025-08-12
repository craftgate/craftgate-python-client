# tests/test_instant_transfer_payment_sample.py
import os
import unittest
import uuid
from decimal import Decimal

from craftgate import Craftgate, RequestOptions
from craftgate.model import ApmAdditionalAction, ApmType, Currency, PaymentGroup, PaymentStatus
from craftgate.request import InitApmPaymentRequest
from craftgate.request.dto import PaymentItem


class InstantTransferPaymentSample(unittest.TestCase):
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
        cls.payment = Craftgate(options).payment()

    def test_retrieve_active_banks(self):
        response = self.payment.retrieve_active_banks()
        print(response)

        self.assertIsNotNone(response.items)
        self.assertTrue(len(response.items) > 0)
        self.assertIsNotNone(response.items[0])

    def test_init_instant_transfer_apm_payment(self):
        items = [
            PaymentItem(name="item 1", external_id=str(uuid.uuid4()), price=Decimal("0.60")),
            PaymentItem(name="item 2", external_id=str(uuid.uuid4()), price=Decimal("0.40"))
        ]

        request = InitApmPaymentRequest(
            apm_type=ApmType.INSTANT_TRANSFER,
            price=Decimal("1"),
            paid_price=Decimal("1"),
            currency=Currency.TRY,
            payment_group=PaymentGroup.LISTING_OR_SUBSCRIPTION,
            conversation_id="456d1297-908e-4bd6-a13b-4be31a6e47d5",
            external_id="optional-externalId",
            callback_url="https://www.your-website.com/craftgate-apm-callback",
            additional_params={"bankCode": "0"},
            items=items
        )

        response = self.payment.init_apm_payment(request)
        print(response)

        self.assertIsNotNone(response.payment_id)
        self.assertIsNone(response.redirect_url)
        self.assertIsNotNone(response.html_content)
        self.assertEqual(PaymentStatus.WAITING, response.payment_status)
        self.assertEqual(ApmAdditionalAction.SHOW_HTML_CONTENT, response.additional_action)


if __name__ == "__main__":
    unittest.main()
