# tests/test_masterpass_payment_sample.py
import os
import unittest
import uuid
from decimal import Decimal

from craftgate.adapter.masterpass_payment_adapter import MasterpassPaymentAdapter
from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.model.payment_phase import PaymentPhase
from craftgate.model.payment_provider import PaymentProvider
from craftgate.request.check_masterpass_user_request import CheckMasterpassUserRequest
from craftgate.request.dto.masterpass_create_payment import MasterpassCreatePayment
from craftgate.request.dto.payment_item import PaymentItem
from craftgate.request.masterpass_payment_complete_request import MasterpassPaymentCompleteRequest
from craftgate.request.masterpass_payment_threeds_complete_request import MasterpassPaymentThreeDSCompleteRequest
from craftgate.request.masterpass_payment_threeds_init_request import MasterpassPaymentThreeDSInitRequest
from craftgate.request.masterpass_payment_token_generate_request import MasterpassPaymentTokenGenerateRequest
from craftgate.request.masterpass_retrieve_loyalties_request import MasterpassRetrieveLoyaltiesRequest
from craftgate.request_options import RequestOptions


class MasterpassSample(unittest.TestCase):
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
        cls.adapter = MasterpassPaymentAdapter(options)

    def test_check_masterpass_user(self):
        request = CheckMasterpassUserRequest(
            masterpass_gsm_number="5305289290"
        )
        response = self.adapter.check_masterpass_user(request)
        print(vars(response))
        self.assertIsNotNone(response)

    def test_generate_masterpass_payment_token(self):
        items = [
            PaymentItem(name="item 1", external_id=str(uuid.uuid4()), price=Decimal("30")),
            PaymentItem(name="item 2", external_id=str(uuid.uuid4()), price=Decimal("50")),
            PaymentItem(name="item 3", external_id=str(uuid.uuid4()), price=Decimal("20")),
        ]
        create_payment = MasterpassCreatePayment(
            price=Decimal("100"),
            paid_price=Decimal("100"),
            installment=1,
            currency=Currency.TRY,
            conversation_id="456d1297-908e-4bd6-a13b-4be31a6e47d5",
            payment_group=PaymentGroup.LISTING_OR_SUBSCRIPTION,
            payment_phase=PaymentPhase.AUTH,
            items=items
        )
        request = MasterpassPaymentTokenGenerateRequest(
            user_id="masterpass-user-id",
            msisdn="5305289290",
            bin_number="404308",
            force_three_d_s=False,
            create_payment=create_payment
        )
        response = self.adapter.generate_masterpass_payment_token(request)
        print(vars(response))
        self.assertIsNotNone(response.reference_id)
        self.assertIsNotNone(response.order_no)
        self.assertIsNotNone(response.token)

    def test_complete_masterpass_payment(self):
        request = MasterpassPaymentCompleteRequest(
            reference_id="83daa370-b935-4477-9be1-6010eb80f986",
            token="20250810052755062OfUa3vz"
        )
        response = self.adapter.complete_masterpass_payment(request)
        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertEqual(PaymentProvider.MASTERPASS, response.payment_provider)
        self.assertIsNone(response.card_user_key)
        self.assertIsNone(response.card_token)
        self.assertIsNone(response.fraud_id)
        self.assertIsNone(response.fraud_action)
        self.assertIsNone(response.payment_error)

    def test_init_3ds_masterpass_payment(self):
        request = MasterpassPaymentThreeDSInitRequest(
            reference_id="referenceId",
            callback_url="https://www.your-website.com/craftgate-3DSecure-callback"
        )
        response = self.adapter.init_3ds_masterpass_payment(request)
        print(vars(response))
        self.assertIsNotNone(response.return_url)

    def test_complete_3ds_masterpass_payment(self):
        request = MasterpassPaymentThreeDSCompleteRequest(
            payment_id=1
        )
        response = self.adapter.complete_3ds_masterpass_payment(request)
        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertEqual(PaymentProvider.MASTERPASS, response.payment_provider)
        self.assertIsNone(response.card_user_key)
        self.assertIsNone(response.card_token)
        self.assertIsNone(response.fraud_id)
        self.assertIsNone(response.fraud_action)
        self.assertIsNone(response.payment_error)

    def test_retrieve_loyalties(self):
        request = MasterpassRetrieveLoyaltiesRequest(
            card_name="YKB Test Kart",
            msisdn="5305289290",
            bin_number="413226"
        )
        response = self.adapter.retrieve_loyalties(request)
        print(vars(response))
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
