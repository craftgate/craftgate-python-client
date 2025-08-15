# tests/test_merchant_sample.py
import os
import unittest

from craftgate import Craftgate, RequestOptions
from craftgate.model import CardAssociation, CardBrand, Currency, PaymentAuthenticationType, \
    PaymentPhase, PosIntegrator, PosOperationType, PosStatus, PosUserType, Status
from craftgate.request import CreateMerchantPosRequest, SearchMerchantPosRequest, UpdateMerchantPosCommissionsRequest, \
    UpdateMerchantPosRequest
from craftgate.request.dto import CreateMerchantPosUser, UpdateMerchantPosCommission, UpdateMerchantPosUser


class MerchantSample(unittest.TestCase):
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
        cls.merchant = Craftgate(options).merchant()

    def test_create_merchant_pos(self):
        create_user = CreateMerchantPosUser(
            pos_operation_type=PosOperationType.STANDARD,
            pos_user_type=PosUserType.API,
            pos_username="username",
            pos_password="password"
        )

        request = CreateMerchantPosRequest(
            name="my test pos",
            client_id="client id",
            terminal_id="terminal id",
            threeds_key="3d secure key",
            status=PosStatus.AUTOPILOT,
            currency=Currency.TRY,
            order_number=1,
            enable_installment=True,
            enable_foreign_card=True,
            enable_payment_without_cvc=True,
            pos_integrator=PosIntegrator.AKBANK,
            enabled_payment_authentication_types=[
                PaymentAuthenticationType.THREE_DS, PaymentAuthenticationType.NON_THREE_DS
            ],
            merchant_pos_users=[create_user]
        )

        resp = self.merchant.create_merchant_pos(request)

        print(vars(resp))
        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp.id)
        self.assertIsNotNone(resp.hostname)
        self.assertIsNotNone(resp.alias)
        self.assertIsNotNone(resp.path)
        self.assertIsNotNone(resp.threeds_path)
        self.assertEqual(resp.pos_integrator, PosIntegrator.AKBANK)

    def test_create_merchant_pos_with_enable_loyalty_flag(self):
        create_user = CreateMerchantPosUser(
            pos_operation_type=PosOperationType.STANDARD,
            pos_user_type=PosUserType.API,
            pos_username="username",
            pos_password="password"
        )

        request = CreateMerchantPosRequest(
            name="my test pos2",
            client_id="client id2",
            terminal_id="terminal id2",
            threeds_key="3d secure key2",
            status=PosStatus.AUTOPILOT,
            currency=Currency.TRY,
            order_number=1,
            enable_installment=True,
            enable_foreign_card=True,
            enable_payment_without_cvc=True,
            enable_loyalty=True,
            pos_integrator=PosIntegrator.AKBANK_VPOS,
            enabled_payment_authentication_types=[
                PaymentAuthenticationType.THREE_DS, PaymentAuthenticationType.NON_THREE_DS
            ],
            merchant_pos_users=[create_user]
        )

        resp = self.merchant.create_merchant_pos(request)

        print(vars(resp))
        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp.id)
        self.assertIsNotNone(resp.hostname)
        self.assertIsNotNone(resp.alias)
        self.assertIsNotNone(resp.path)
        self.assertIsNotNone(resp.threeds_path)
        self.assertEqual(resp.pos_integrator, PosIntegrator.AKBANK_VPOS)

    def test_update_merchant_pos(self):
        merchant_pos_id = 3353325

        pos_user = UpdateMerchantPosUser(
            id=52612,
            pos_operation_type=PosOperationType.STANDARD,
            pos_user_type=PosUserType.API,
            pos_username="username",
            pos_password="password"
        )

        request = UpdateMerchantPosRequest(
            name="my updated test pos",
            hostname="https://www.sanalakpos.com",
            client_id="updated client id",
            terminal_id="terminal id",
            mode="P",
            path="/fim/api",
            port=443,
            threeds_key="3d secure key",
            threeds_path="https://www.sanalakpos.com/fim/est3dgate",
            enable_foreign_card=True,
            enable_installment=True,
            enable_payment_without_cvc=True,
            new_integration=False,
            order_number=1,
            enabled_payment_phases=[PaymentPhase.AUTH],
            enabled_payment_authentication_types=[
                PaymentAuthenticationType.THREE_DS, PaymentAuthenticationType.NON_THREE_DS
            ],
            supported_card_associations=[CardAssociation.MASTER_CARD, CardAssociation.VISA],
            merchant_pos_users=[pos_user]
        )

        resp = self.merchant.update_merchant_pos(merchant_pos_id, request)
        print(vars(resp))
        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp.id)
        self.assertIsNotNone(resp.hostname)
        self.assertIsNotNone(resp.alias)
        self.assertIsNotNone(resp.path)
        self.assertIsNotNone(resp.threeds_path)

    def test_update_merchant_pos_status(self):
        merchant_pos_id = 3353325
        self.merchant.update_merchant_pos_status(merchant_pos_id, PosStatus.PASSIVE)
        self.assertTrue(True)

    def test_retrieve_merchant_pos(self):
        merchant_pos_id = 3353325
        resp = self.merchant.retrieve(merchant_pos_id)

        print(vars(resp))
        self.assertIsNotNone(resp)
        self.assertEqual(resp.id, merchant_pos_id)

    def test_delete_merchant_pos(self):
        merchant_pos_id = 3353325
        self.merchant.delete_merchant_pos(merchant_pos_id)
        self.assertTrue(True)

    def test_search_merchant_poses(self):
        request = SearchMerchantPosRequest(
            currency=Currency.TRY,
            page=0,
            size=10
        )
        resp = self.merchant.search_merchant_pos(request)

        print(vars(resp))
        self.assertIsNotNone(resp)
        self.assertEqual(resp.page, 0)
        self.assertEqual(resp.size, 10)
        self.assertIsNotNone(resp.items)

    def test_retrieve_merchant_pos_commissions(self):
        merchant_pos_id = 3353326
        resp = self.merchant.retrieve_merchant_pos_commissions(merchant_pos_id)

        print(vars(resp))
        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp.items)

    def test_update_merchant_pos_commissions(self):
        merchant_pos_id = 3353326

        installment1 = UpdateMerchantPosCommission(
            installment=1,
            blockage_day=7,
            status=Status.ACTIVE,
            card_brand_name=CardBrand.AXESS,
            installment_label="Single installment",
            bank_on_us_debit_card_commission_rate=1.0,
            bank_on_us_credit_card_commission_rate=1.1,
            bank_not_on_us_debit_card_commission_rate=1.2,
            bank_not_on_us_credit_card_commission_rate=1.3,
            bank_foreign_card_commission_rate=1.5
        )

        installment2 = UpdateMerchantPosCommission(
            installment=2,
            blockage_day=7,
            status=Status.ACTIVE,
            card_brand_name=CardBrand.AXESS,
            installment_label="installment 2",
            bank_on_us_credit_card_commission_rate=2.1,
            merchant_commission_rate=2.3
        )

        request = UpdateMerchantPosCommissionsRequest(
            commissions=[installment1, installment2]
        )

        resp = self.merchant.update_merchant_pos_commissions(merchant_pos_id, request)

        print(vars(resp))
        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp.items)


if __name__ == "__main__":
    unittest.main()
