# tests/test_bkm_express_payment_sample.py
import os
import unittest
from craftgate import Craftgate

from craftgate.adapter.bkm_express_payment_adapter import BkmExpressPaymentAdapter
from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.request.complete_bkm_express_request import CompleteBkmExpressRequest
from craftgate.request.dto.payment_item import PaymentItem
from craftgate.request.init_bkm_express_request import InitBkmExpressRequest
from craftgate.request_options import RequestOptions
from craftgate.utils.converter import Converter


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

    def test_init_bkm_express(self):
        items = [
            PaymentItem(name="Item 1", price=30.0, external_id="123d1297-839e-4bd6-a13b-4be31a6e12a8"),
            PaymentItem(name="Item 2", price=50.0, external_id="789d1297-839e-4bd6-a13b-4be31a6e13f7"),
            PaymentItem(name="Item 3", price=20.0, external_id="3a1d1297-839e-4bd6-a13b-4be31a6e18e6"),
        ]

        request = InitBkmExpressRequest(
            price=100.0,
            paid_price=100.0,
            conversation_id="456d1297-908e-4bd6-a13b-4be31a6e47d5",
            currency=Currency.TRY,
            payment_group=PaymentGroup.LISTING_OR_SUBSCRIPTION,
            items=items
        )

        response = self.bkm_express_payment.init(request)

        print(Converter.to_clean_dict(response))
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.token)
        self.assertIsNotNone(response.path)
        self.assertIsNotNone(response.id)

    def test_complete_bkm_express(self):
        ticket_id = os.environ.get("BKM_TICKET_ID", "ce6d93c3-b399-406d-8efc-fdba0b37768c")

        request = CompleteBkmExpressRequest(
            status=True,
            message="İşlem başarılı",
            ticket_id=ticket_id
        )

        response = self.bkm_express_payment.complete(request)
        print(Converter.to_clean_dict(response))
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.order_id)

    def test_retrieve_payment_by_ticket_id(self):
        ticket_id = os.environ.get("BKM_TICKET_ID", "ce6d93c3-b399-406d-8efc-fdba0b37768c")

        response = self.bkm_express_payment.retrieve_payment(ticket_id)
        print(Converter.to_clean_dict(response))
        self.assertIsNotNone(response)

    def test_retrieve_payment_by_token(self):
        token = os.environ.get("BKM_TOKEN", "cb90071c-1f2c-4fb7-9049-c5f13f9f7286")

        response = self.bkm_express_payment.retrieve_payment_by_token(token)
        print(Converter.to_clean_dict(response))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
