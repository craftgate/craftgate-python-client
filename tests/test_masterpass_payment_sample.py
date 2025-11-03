# tests/test_masterpass_payment_sample.py
import os
import unittest
import uuid
from decimal import Decimal

from craftgate import Craftgate, RequestOptions
from craftgate.model import Currency, PaymentGroup, PaymentPhase, PaymentProvider
from craftgate.request import CheckMasterpassUserRequest, MasterpassPaymentCompleteRequest, \
    MasterpassPaymentThreeDSCompleteRequest, MasterpassPaymentThreeDSInitRequest, MasterpassPaymentTokenGenerateRequest, \
    MasterpassRetrieveLoyaltiesRequest, MasterpassCreatePayment, PaymentItem


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
        cls.masterpass_payment = Craftgate(options).masterpass_payment()

    def test_check_masterpass_user(self):
        request = CheckMasterpassUserRequest(
            masterpass_gsm_number="5550001122"
        )
        response = self.masterpass_payment.check_masterpass_user(request)
        print(response)
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
        response = self.masterpass_payment.generate_masterpass_payment_token(request)
        print(response)

        self.assertIsNotNone(response.reference_id)
        self.assertIsNotNone(response.order_no)
        self.assertIsNotNone(response.token)

    def test_complete_masterpass_payment(self):
        request = MasterpassPaymentCompleteRequest(
            reference_id="83daa370-b935-4477-9be1-6010eb80f986",
            token="20250810052755062OfUa3vz"
        )
        response = self.masterpass_payment.complete_masterpass_payment(request)
        print(response)

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
        response = self.masterpass_payment.init_3ds_masterpass_payment(request)
        print(response)
        self.assertIsNotNone(response.return_url)

    def test_complete_3ds_masterpass_payment(self):
        request = MasterpassPaymentThreeDSCompleteRequest(
            payment_id=1
        )
        response = self.masterpass_payment.complete_3ds_masterpass_payment(request)
        print(response)

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
        response = self.masterpass_payment.retrieve_loyalties(request)
        print(response)
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
