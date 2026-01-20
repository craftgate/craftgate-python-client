# tests/test_payment_sample.py
import os
import unittest
import uuid
from decimal import Decimal

from craftgate import Craftgate, RequestOptions, PaymentTransaction, FraudCheckParameters
from craftgate.model import AdditionalAction, ApmAdditionalAction, ApmType, CardAssociation, CardProvider, CardType, \
    Currency, Loyalty, LoyaltyParams, LoyaltyType, PaymentGroup, PaymentPhase, PaymentStatus, PaymentType, \
    PosApmPaymentProvider, RefundDestinationType, RefundStatus, Reward, WalletTransactionType
from craftgate.request import ApprovePaymentTransactionsRequest, CloneCardRequest, CompleteApmPaymentRequest, \
    CompletePosApmPaymentRequest, CompleteThreeDSPaymentRequest, CreateApmPaymentRequest, CreateDepositPaymentRequest, \
    CreateFundTransferDepositPaymentRequest, CreatePaymentRequest, DeleteStoredCardRequest, \
    DisapprovePaymentTransactionsRequest, Card, GarantiPayInstallment, PaymentItem, InitApmDepositPaymentRequest, \
    InitApmPaymentRequest, InitCheckoutPaymentRequest, InitGarantiPayPaymentRequest, InitPosApmPaymentRequest, \
    InitThreeDSPaymentRequest, PostAuthPaymentRequest, RefundPaymentRequest, \
    RefundPaymentTransactionMarkAsRefundedRequest, RefundPaymentTransactionRequest, RetrieveLoyaltiesRequest, \
    RetrieveProviderCardRequest, SearchStoredCardsRequest, StoreCardRequest, UpdateCardRequest, \
    UpdatePaymentTransactionRequest
from craftgate.response import MultiPaymentResponse, PaymentTransactionApprovalListResponse, PaymentTransactionResponse, \
    StoredCardListResponse


class PaymentSample(unittest.TestCase):
    API_KEY = os.environ.get("CG_API_KEY", "zG5jvjwWQyo3iIDyr6p1tvy1DzTXfnTb")
    SECRET_KEY = os.environ.get("CG_SECRET_KEY", "yzyiMbQD8cNGh6qHWbP0rLE56LDdmh8J")
    BASE_URL = os.environ.get("CG_BASE_URL", "http://localhost:8000")

    @classmethod
    def setUpClass(cls):
        options = RequestOptions(
            api_key=cls.API_KEY,
            secret_key=cls.SECRET_KEY,
            base_url=cls.BASE_URL
        )
        cls.payment = Craftgate(options).payment()

    def test_create_payment(self):
        items = []

        pi1 = PaymentItem()
        pi1.name = "item 1"
        pi1.external_id = str(uuid.uuid4())
        pi1.price = Decimal("30")
        items.append(pi1)

        pi2 = PaymentItem()
        pi2.name = "item 2"
        pi2.external_id = str(uuid.uuid4())
        pi2.price = Decimal("50")
        items.append(pi2)

        pi3 = PaymentItem()
        pi3.name = "item 3"
        pi3.external_id = str(uuid.uuid4())
        pi3.price = Decimal("20")
        items.append(pi3)

        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "5258640000000001"
        card.expire_year = "2044"
        card.expire_month = "07"
        card.cvc = "000"

        req = CreatePaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.create_payment(req)
        print(resp)

        self.assertIsNotNone(resp)
        self.assertEqual(resp.payment_status, PaymentStatus.SUCCESS)
        self.assertIsInstance(resp.payment_transactions[0], PaymentTransaction)

    def test_create_marketplace_payment(self):
        items = []

        pi1 = PaymentItem()
        pi1.name = "item 1"
        pi1.external_id = str(uuid.uuid4())
        pi1.price = Decimal("30")
        pi1.sub_merchant_member_id = 116212
        pi1.sub_merchant_member_price = Decimal("27")
        items.append(pi1)

        pi2 = PaymentItem()
        pi2.name = "item 2"
        pi2.external_id = str(uuid.uuid4())
        pi2.price = Decimal("50")
        pi2.sub_merchant_member_id = 116212
        pi2.sub_merchant_member_price = Decimal("42")
        items.append(pi2)

        pi3 = PaymentItem()
        pi3.name = "item 3"
        pi3.external_id = str(uuid.uuid4())
        pi3.price = Decimal("20")
        pi3.sub_merchant_member_id = 116212
        pi3.sub_merchant_member_price = Decimal("18")
        items.append(pi3)

        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "5258640000000001"
        card.expire_year = "2044"
        card.expire_month = "07"
        card.cvc = "000"

        req = CreatePaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.PRODUCT
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.create_payment(req)
        print(resp)
        self.assertIsNotNone(resp)

    def test_create_payment_and_store_card(self):
        items = []
        for name, price in [("item 1", "30"), ("item 2", "50"), ("item 3", "20")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "5258640000000001"
        card.expire_year = "2044"
        card.expire_month = "07"
        card.cvc = "000"
        card.store_card_after_success_payment = True
        card.card_alias = "My YKB Card"

        req = CreatePaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.external_id = "external_id-123456789"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.create_payment(req)
        print(resp)
        self.assertIsNotNone(resp)

    def test_create_payment_using_stored_card(self):
        items = []
        for name, price in [("item 1", "30"), ("item 2", "50"), ("item 3", "20")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        card = Card()
        card.card_user_key = "63528179-30ea-4d4e-8751-8b59794f3300"
        card.card_token = "682059fb-d935-44e9-9f9d-6139abf150bf"

        req = CreatePaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.create_payment(req)
        print(resp)
        self.assertIsNotNone(resp)

    def test_create_payment_using_external_payment_provider_stored_card(self):
        items = []
        for name, price in [("item 1", "30"), ("item 2", "50"), ("item 3", "20")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = CreatePaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.pos_alias = "67-ykb-3353340"
        req.installment = 1
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.external_id = "external_id-123456789"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.items = items
        req.additional_params = {
            "paymentProvider": {
                "cardUserKey": "63528179-30ea-4d4e-8751-8b59794f3300",
                "cardToken": "682059fb-d935-44e9-9f9d-6139abf150bf"
            }
        }

        resp = self.payment.create_payment(req)
        print(resp)
        self.assertIsNotNone(resp)

    def test_create_payment_with_loyalty(self):
        items = []
        for name, price in [("item 1", "30"), ("item 2", "50"), ("item 3", "20")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "4043080000000003"
        card.expire_year = "2044"
        card.expire_month = "07"
        card.cvc = "000"

        loyalty = Loyalty()
        loyalty.type = LoyaltyType.REWARD_MONEY
        reward = Reward()
        reward.card_reward_money = Decimal("1.36")
        reward.firm_reward_money = Decimal("3.88")
        loyalty.reward = reward
        card.loyalty = loyalty

        req = CreatePaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.create_payment(req)
        print(resp)
        self.assertIsNotNone(resp)

    def test_create_payment_with_postponing_payment_loyalty(self):
        items = []
        for name, price in [("item 1", "30"), ("item 2", "50"), ("item 3", "20")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "9792675000000002"
        card.expire_year = "2027"
        card.expire_month = "06"
        card.cvc = "000"

        loyalty = Loyalty()
        loyalty.type = LoyaltyType.POSTPONING_PAYMENT
        params = LoyaltyParams()
        params.postponing_payment_count = 90
        loyalty.loyalty_params = params
        card.loyalty = loyalty

        req = CreatePaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.create_payment(req)
        print(resp)
        self.assertIsNotNone(resp)

    def test_create_payment_with_first6_last4_and_identity_number(self):
        items = []
        pi = PaymentItem()
        pi.name = "item 1"
        pi.external_id = str(uuid.uuid4())
        pi.price = Decimal("100")
        items.append(pi)

        card = Card()
        card.card_holder_identity_number = "12345678900"
        card.bin_number = "404308"
        card.last_four_digits = "0003"

        req = CreatePaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.create_payment(req)
        print(resp)
        self.assertIsNotNone(resp)

    def test_init_3ds_payment(self):
        items = []
        for name, price in [("item 1", "30"), ("item 2", "50"), ("item 3", "20")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "5258640000000001"
        card.expire_year = "2044"
        card.expire_month = "07"
        card.cvc = "000"

        req = InitThreeDSPaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.callback_url = "https://www.your-website.com/craftgate-3DSecure-callback"
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.init_3ds_payment(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(getattr(resp, "html_content", None))
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNotNone(getattr(resp, "redirect_url", None))

    def test_init_3ds_marketplace_payment(self):
        items = []

        pi1 = PaymentItem()
        pi1.name = "item 1"
        pi1.external_id = str(uuid.uuid4())
        pi1.price = Decimal("30")
        pi1.sub_merchant_member_id = 116212
        pi1.sub_merchant_member_price = Decimal("27")
        items.append(pi1)

        pi2 = PaymentItem()
        pi2.name = "item 2"
        pi2.external_id = str(uuid.uuid4())
        pi2.price = Decimal("50")
        pi2.sub_merchant_member_id = 116212
        pi2.sub_merchant_member_price = Decimal("42")
        items.append(pi2)

        pi3 = PaymentItem()
        pi3.name = "item 3"
        pi3.external_id = str(uuid.uuid4())
        pi3.price = Decimal("20")
        pi3.sub_merchant_member_id = 116212
        pi3.sub_merchant_member_price = Decimal("18")
        items.append(pi3)

        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "5258640000000001"
        card.expire_year = "2044"
        card.expire_month = "07"
        card.cvc = "000"

        req = InitThreeDSPaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.callback_url = "https://www.your-website.com/craftgate-3DSecure-callback"
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.PRODUCT
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.init_3ds_payment(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(getattr(resp, "html_content", None))
        self.assertIsNotNone(getattr(resp, "payment_id", None))

    def test_init_3ds_payment_and_store_card(self):
        items = []
        for name, price in [("item 1", "30"), ("item 2", "50"), ("item 3", "20")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "5258640000000001"
        card.expire_year = "2044"
        card.expire_month = "07"
        card.cvc = "000"
        card.store_card_after_success_payment = True
        card.card_alias = "My YKB Card"

        req = InitThreeDSPaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.callback_url = "https://www.your-website.com/craftgate-3DSecure-callback"
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.init_3ds_payment(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(getattr(resp, "html_content", None))
        self.assertIsNotNone(getattr(resp, "payment_id", None))

    def test_init_3ds_payment_using_stored_card(self):
        items = []
        for name, price in [("item 1", "30"), ("item 2", "50"), ("item 3", "20")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        card = Card()
        card.card_user_key = "63528179-30ea-4d4e-8751-8b59794f3300"
        card.card_token = "682059fb-d935-44e9-9f9d-6139abf150bf"

        req = InitThreeDSPaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.callback_url = "https://www.your-website.com/craftgate-3DSecure-callback"
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.init_3ds_payment(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(getattr(resp, "html_content", None))
        self.assertIsNotNone(getattr(resp, "payment_id", None))

    def test_complete_3ds_payment(self):
        req = CompleteThreeDSPaymentRequest()
        req.payment_id = 1291818

        resp = self.payment.complete_3ds_payment(req)
        print(resp)
        self.assertIsNotNone(resp)

    def test_init_checkout_payment(self):
        items = []
        for name, price in [("item 1", "30"), ("item 2", "50"), ("item 3", "20")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitCheckoutPaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.buyer_member_id = 116211
        req.callback_url = "https://www.your-website.com/craftgate-checkout-callback"
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.items = items

        resp = self.payment.init_checkout_payment(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(getattr(resp, "page_url", None))
        self.assertIsNotNone(getattr(resp, "token", None))
        self.assertIsNotNone(getattr(resp, "token_expire_date", None))

    def test_init_checkout_payment_for_deposit(self):
        req = InitCheckoutPaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.buyer_member_id = 116211
        req.callback_url = "https://www.your-website.com/craftgate-checkout-callback"
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.PRODUCT
        req.payment_phase = PaymentPhase.AUTH
        req.deposit_payment = True

        resp = self.payment.init_checkout_payment(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(getattr(resp, "page_url", None))
        self.assertIsNotNone(getattr(resp, "token", None))
        self.assertIsNotNone(getattr(resp, "token_expire_date", None))

    def test_retrieve_checkout_payment(self):
        token = "5097ec00-ce50-4b56-82d3-6c2f86231ef2"
        resp = self.payment.retrieve_checkout_payment(token)
        print(resp)
        self.assertIsNotNone(resp)

    def test_expire_checkout_payment(self):
        token = "a768c57c-5052-4038-857f-1e2cf54253bc"
        self.payment.expire_checkout_payment(token)

    def test_create_deposit_payment(self):
        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "5258640000000001"
        card.expire_year = "2044"
        card.expire_month = "07"
        card.cvc = "000"

        req = CreateDepositPaymentRequest()
        req.price = Decimal("100")
        req.buyer_member_id = 116211
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.card = card

        resp = self.payment.create_deposit_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "id", None))
        self.assertEqual(req.buyer_member_id, resp.buyer_member_id)
        self.assertEqual(req.price, resp.price)
        self.assertEqual(PaymentStatus.SUCCESS, resp.payment_status)
        self.assertEqual(PaymentType.DEPOSIT_PAYMENT, resp.payment_type)

    def test_init_3ds_deposit_payment(self):
        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "5258640000000001"
        card.expire_year = "2044"
        card.expire_month = "07"
        card.cvc = "000"

        req = CreateDepositPaymentRequest()
        req.price = Decimal("100")
        req.buyer_member_id = 116211
        req.callback_url = "https://www.your-website.com/craftgate-3DSecure-callback"
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.card = card

        resp = self.payment.init_3ds_deposit_payment(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(getattr(resp, "html_content", None))
        self.assertIsNotNone(getattr(resp, "payment_id", None))

    def test_complete_3ds_deposit_payment(self):
        req = CompleteThreeDSPaymentRequest()
        req.payment_id = 1

        resp = self.payment.complete_3ds_deposit_payment(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(Decimal("100"), resp.price)
        self.assertEqual(PaymentStatus.SUCCESS, resp.payment_status)
        self.assertEqual(PaymentType.DEPOSIT_PAYMENT, resp.payment_type)

    def test_create_fund_transfer_deposit_payment(self):
        req = CreateFundTransferDepositPaymentRequest()
        req.price = Decimal("100")
        req.buyer_member_id = 1
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"

        resp = self.payment.create_fund_transfer_deposit_payment(req)
        print(resp)
        self.assertEqual(req.buyer_member_id, resp.buyer_member_id)
        self.assertEqual(Decimal("100.00000000"), resp.price)
        self.assertEqual(req.conversation_id, resp.conversation_id)
        self.assertIsNotNone(getattr(resp, "wallet_transaction", None))
        self.assertEqual(
            WalletTransactionType.DEPOSIT_FROM_FUND_TRANSFER,
            resp.wallet_transaction.wallet_transaction_type
        )

    def test_init_apm_deposit_payment(self):
        req = InitApmDepositPaymentRequest()
        req.apm_type = ApmType.PAPARA
        req.price = Decimal("1")
        req.currency = Currency.TRY
        req.buyer_member_id = 1
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.external_id = "optional-externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.client_ip = "127.0.0.1"

        resp = self.payment.init_apm_deposit_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNotNone(getattr(resp, "redirect_url", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.REDIRECT_TO_URL, resp.additional_action)

    def test_init_garanti_pay_payment(self):
        items = []
        for name, price in [("item 1", "30"), ("item 2", "50"), ("item 3", "20")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        installments = []
        inst2 = GarantiPayInstallment()
        inst2.number = 2
        inst2.total_price = Decimal("120")
        installments.append(inst2)

        inst3 = GarantiPayInstallment()
        inst3.number = 3
        inst3.total_price = Decimal("125")
        installments.append(inst3)

        req = InitGarantiPayPaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.callback_url = "https://www.your-website.com/craftgate-garantipay-callback"
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.items = items
        req.installments = installments
        req.enabled_installments = [2, 3]

        resp = self.payment.init_garanti_pay_payment(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(getattr(resp, "html_content", None))
        self.assertIsNotNone(getattr(resp, "payment_id", None))

    def test_init_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.60"), ("item 2", "0.40")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.PAPARA
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.external_id = "optional-externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.items = items

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNotNone(getattr(resp, "redirect_url", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.REDIRECT_TO_URL, resp.additional_action)

    def test_init_sodexo_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.60"), ("item 2", "0.40")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.SODEXO
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.external_id = "optional-externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.apm_user_identity = "5555555555"
        req.items = items
        req.additional_params = {"sodexoCode": "843195"}

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNone(getattr(resp, "redirect_url", None))
        self.assertEqual(PaymentStatus.SUCCESS, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.NONE, resp.additional_action)

    def test_init_edenred_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.60"), ("item 2", "0.40")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.EDENRED
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.external_id = "optional-externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.apm_user_identity = "6036819041742253"
        req.items = items

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNone(getattr(resp, "redirect_url", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.OTP_REQUIRED, resp.additional_action)

    def test_complete_edenred_apm_payment(self):
        req = CompleteApmPaymentRequest()
        req.payment_id = 1
        req.additional_params = {"otpCode": "784294"}

        resp = self.payment.complete_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertEqual(PaymentStatus.SUCCESS, resp.payment_status)

    def test_init_paypal_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.60"), ("item 2", "0.40")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.PAYPAL
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.USD
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.external_id = "optional-externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.items = items

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNone(getattr(resp, "redirect_url", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.REDIRECT_TO_URL, resp.additional_action)

    def test_init_iwallet_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.60"), ("item 2", "0.40")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.IWALLET
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.external_id = "optional-externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.additional_params = {"cardNumber": "1111222233334444"}
        req.items = items

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNone(getattr(resp, "redirect_url", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.OTP_REQUIRED, resp.additional_action)

    def test_complete_iwallet_apm_payment(self):
        req = CompleteApmPaymentRequest()
        req.payment_id = 1
        req.additional_params = {"passCode": "1122"}

        resp = self.payment.complete_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertEqual(PaymentStatus.SUCCESS, resp.payment_status)

    def test_init_klarna_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.60"), ("item 2", "0.40")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.KLARNA
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.EUR
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.external_id = "optional-externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.items = items
        req.additional_params = {"country": "de", "locale": "en-DE"}

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNotNone(getattr(resp, "redirect_url", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.REDIRECT_TO_URL, resp.additional_action)

    def test_init_afterpay_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.6"), ("item 2", "0.4")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.AFTERPAY
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.USD
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.external_id = "optional-externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.items = items

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNotNone(getattr(resp, "redirect_url", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.REDIRECT_TO_URL, resp.additional_action)

    def test_init_metropol_apm_payment(self):
        items = []
        pi = PaymentItem()
        pi.name = "item 1"
        pi.external_id = str(uuid.uuid4())
        pi.price = Decimal("1.00")
        items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.METROPOL
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "myConversationId"
        req.external_id = "optional-externalId"
        req.items = items
        req.additional_params = {"cardNumber": "6375780115068760"}

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNotNone(getattr(resp, "additional_data", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.OTP_REQUIRED, resp.additional_action)

    def test_complete_metropol_apm_payment(self):
        req = CompleteApmPaymentRequest()
        req.payment_id = 1
        req.additional_params = {
            "otpCode": "00000",
            "productId": "1",
            "walletId": "1",
        }

        resp = self.payment.complete_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertEqual(PaymentStatus.SUCCESS, resp.payment_status)

    def test_init_kaspi_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.6"), ("item 2", "0.4")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.KASPI
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.KZT
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.external_id = "optional-externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.items = items

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNotNone(getattr(resp, "redirect_url", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.REDIRECT_TO_URL, resp.additional_action)

    def test_init_tompay_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.6"), ("item 2", "0.4")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.TOMPAY
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "conversationId"
        req.external_id = "externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.items = items
        req.additional_params = {"channel": "channel", "phone": "5001112233"}

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.WAIT_FOR_WEBHOOK, resp.additional_action)

    def test_init_chippin_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.6"), ("item 2", "0.4")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.CHIPPIN
        req.apm_user_identity = "1000000"
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "conversationId"
        req.external_id = "externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.items = items

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.WAIT_FOR_WEBHOOK, resp.additional_action)

    def test_init_bizum_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.6"), ("item 2", "0.4")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.BIZUM
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.EUR
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "conversationId"
        req.external_id = "externalId"
        req.additional_params = {"buyerPhoneNumber": "34700000000"}
        req.items = items

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.WAIT_FOR_WEBHOOK, resp.additional_action)

    def test_init_mbway_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.6"), ("item 2", "0.4")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.PAYLANDS_MB_WAY
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.EUR
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "conversationId"
        req.external_id = "externalId"
        req.additional_params = {"buyerPhoneNumber": "34700000000"}
        req.items = items

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.WAIT_FOR_WEBHOOK, resp.additional_action)

    def test_init_paycell_dcb_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.6"), ("item 2", "0.4")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.PAYCELL_DCB
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "conversationId"
        req.external_id = "externalId"
        req.callback_url = "callback"
        req.additional_params = {"paycellGsmNumber": "5305289290"}
        req.items = items

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.OTP_REQUIRED, resp.additional_action)

    def test_init_paymob_apm_payment(self):
        items = []
        pi = PaymentItem()
        pi.name = "item 1"
        pi.external_id = str(uuid.uuid4())
        pi.price = Decimal("10")
        items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.PAYMOB
        req.price = Decimal("10")
        req.paid_price = Decimal("10")
        req.currency = Currency.EGP
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "conversationId"
        req.external_id = "externalId"
        req.callback_url = "https://www.your-website.com/craftgate-apm-callback"
        req.items = items
        req.additional_params = {"integrationId": "11223344"}

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.REDIRECT_TO_URL, resp.additional_action)

    def test_init_ykb_world_pay_pos_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.6"), ("item 2", "0.4")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitPosApmPaymentRequest()
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_provider = PosApmPaymentProvider.YKB_WORLD_PAY
        req.additional_params = {"sourceCode": "WEB2QR"}
        req.callback_url = "https://www.your-website.com/craftgate-pos-apm-callback"
        req.items = items

        resp = self.payment.init_pos_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNotNone(getattr(resp, "html_content", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(AdditionalAction.SHOW_HTML_CONTENT, resp.additional_action)

    def test_init_garanti_pay_pos_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.6"), ("item 2", "0.4")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitPosApmPaymentRequest()
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_provider = PosApmPaymentProvider.GARANTI_PAY
        req.additional_params = {"integrationType": "WEB2APP"}
        req.callback_url = "https://www.your-website.com/craftgate-pos-apm-callback"
        req.items = items

        resp = self.payment.init_pos_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertIsNotNone(resp.additional_data.get("redirectUrl"))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(AdditionalAction.REDIRECT_TO_URL, resp.additional_action)

    def test_init_setcard_apm_payment(self):
        items = []
        for name, price in [("item 1", "0.6"), ("item 2", "0.4")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = InitApmPaymentRequest()
        req.apm_type = ApmType.SETCARD
        req.price = Decimal("1")
        req.paid_price = Decimal("1")
        req.currency = Currency.TRY
        req.callback_url = "https://www.your-website.com/craftgate-3DSecure-callback"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "conversationId"
        req.external_id = "externalId"
        req.additional_params = {"cardNumber": "7599640961180814"}
        req.items = items

        resp = self.payment.init_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertEqual(PaymentStatus.WAITING, resp.payment_status)
        self.assertEqual(ApmAdditionalAction.OTP_REQUIRED, resp.additional_action)

    def test_complete_setcard_pos_apm_payment(self):
        req = CompleteApmPaymentRequest()
        req.payment_id = 1
        req.additional_params = {"otpCode": "123456"}

        resp = self.payment.complete_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "payment_id", None))
        self.assertEqual(PaymentStatus.SUCCESS, resp.payment_status)

    def test_complete_pos_apm_payment(self):
        req = CompletePosApmPaymentRequest()
        req.payment_id = 1

        resp = self.payment.complete_pos_apm_payment(req)
        print(resp)
        self.assertIsNotNone(resp)

    def test_create_cash_on_delivery_payment(self):
        items = []
        for name, price in [("item 1", "60"), ("item 2", "40")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = CreateApmPaymentRequest()
        req.apm_type = ApmType.CASH_ON_DELIVERY
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "241cf73c-7ef1-4e29-a6cc-f37905f2fc3d"
        req.external_id = "optional-externalId"
        req.items = items

        resp = self.payment.create_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "id", None))
        self.assertEqual(Decimal("100.00000000"), resp.price)
        self.assertEqual(PaymentStatus.SUCCESS, resp.payment_status)
        self.assertEqual(PaymentType.APM, resp.payment_type)
        self.assertEqual("241cf73c-7ef1-4e29-a6cc-f37905f2fc3d", resp.conversation_id)
        self.assertEqual(2, len(resp.payment_transactions))

    def test_create_fund_transfer_payment(self):
        items = []
        for name, price in [("item 1", "60"), ("item 2", "40")]:
            pi = PaymentItem()
            pi.name = name
            pi.external_id = str(uuid.uuid4())
            pi.price = Decimal(price)
            items.append(pi)

        req = CreateApmPaymentRequest()
        req.apm_type = ApmType.FUND_TRANSFER
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.currency = Currency.TRY
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.conversation_id = "2bc39889-b34f-40b0-abb0-4ab344360705"
        req.external_id = "optional-externalId"
        req.items = items

        resp = self.payment.create_apm_payment(req)
        print(resp)
        self.assertIsNotNone(getattr(resp, "id", None))
        self.assertEqual(Decimal("100.00000000"), resp.price)
        self.assertEqual(PaymentStatus.SUCCESS, resp.payment_status)
        self.assertEqual(PaymentType.APM, resp.payment_type)
        self.assertEqual("2bc39889-b34f-40b0-abb0-4ab344360705", resp.conversation_id)
        self.assertEqual(2, len(resp.payment_transactions))

    def test_retrieve_payment_by_id(self):
        payment_id = 1
        resp = self.payment.retrieve_payment(payment_id)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(payment_id, resp.id)

    def test_retrieve_loyalties(self):
        req = RetrieveLoyaltiesRequest()
        req.card_number = "4043080000000003"
        req.expire_year = "2044"
        req.expire_month = "07"
        req.cvc = "000"

        req.client_ip = "127.0.0.1"
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.fraud_params = FraudCheckParameters()
        req.fraud_params.buyer_email = "buyer@email.com"
        req.fraud_params.buyer_phone_number = "905555555555"
        req.fraud_params.buyer_external_id = "buyerExternalId444"
        req.fraud_params.custom_fraud_variable = "sessionId213123"

        resp = self.payment.retrieve_loyalties(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual("Bonus", resp.card_brand)
        self.assertIsNotNone(resp.loyalties)
        self.assertGreater(len(resp.loyalties), 0)
        self.assertEqual(LoyaltyType.REWARD_MONEY, resp.loyalties[0].type)
        self.assertIsNotNone(resp.loyalties[0].reward)
        self.assertEqual(Decimal("12.35"), resp.loyalties[0].reward.card_reward_money)
        self.assertEqual(Decimal("5.20"), resp.loyalties[0].reward.firm_reward_money)

    def test_refund_payment(self):
        req = RefundPaymentRequest()
        req.payment_id = 1
        req.refund_destination_type = RefundDestinationType.PROVIDER

        resp = self.payment.refund_payment(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(req.payment_id, resp.payment_id)
        self.assertEqual(RefundStatus.SUCCESS, resp.status)

    def test_retrieve_payment_refund(self):
        payment_refund_id = 1
        resp = self.payment.retrieve_payment_refund(payment_refund_id)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(payment_refund_id, resp.id)

    def test_refund_payment_transaction(self):
        req = RefundPaymentTransactionRequest()
        req.payment_transaction_id = 1
        req.refund_price = Decimal("20")
        req.refund_destination_type = RefundDestinationType.PROVIDER
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"

        resp = self.payment.refund_payment_transaction(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(req.payment_transaction_id, resp.payment_transaction_id)
        self.assertEqual(RefundStatus.SUCCESS, resp.status)

    def test_retrieve_payment_transaction_refund(self):
        payment_transaction_refund_id = 1

        resp = self.payment.retrieve_payment_transaction_refund(payment_transaction_refund_id)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(payment_transaction_refund_id, resp.id)
        self.assertEqual(RefundStatus.SUCCESS, resp.status)

    def test_refund_payment_transaction_mark_as_refunded(self):
        req = RefundPaymentTransactionMarkAsRefundedRequest()
        req.payment_transaction_id = 1
        req.refund_price = Decimal("20")

        resp = self.payment.refund_payment_transaction_mark_as_refunded(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(RefundStatus.SUCCESS, resp.status)

    def test_refund_payment_mark_as_refunded(self):
        req = RefundPaymentRequest()
        req.payment_id = 1024
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"

        resp = self.payment.refund_payment_mark_as_refunded(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertTrue(len(resp.items) > 0)

    def test_store_card(self):
        req = StoreCardRequest()
        req.card_holder_name = "Haluk Demir"
        req.card_number = "5258640000000001"
        req.expire_year = "2044"
        req.expire_month = "07"
        req.card_alias = "My Other Cards"

        resp = self.payment.store_card(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp.card_token)
        self.assertIsNotNone(resp.card_user_key)
        self.assertIsNotNone(resp.created_at)
        self.assertEqual("525864", resp.bin_number)
        self.assertEqual("0001", resp.last_four_digits)
        self.assertEqual("My Other Cards", resp.card_alias)
        self.assertEqual("Haluk Demir", resp.card_holder_name)

    def test_store_card_with_secure_fields(self):
        req = StoreCardRequest()
        req.secure_fields_token = "xxXXxx"

        resp = self.payment.store_card(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp.card_token)
        self.assertIsNotNone(resp.card_user_key)
        self.assertIsNotNone(resp.created_at)

    def test_update_stored_card(self):
        req = UpdateCardRequest()
        req.card_user_key = "fac377f2-ab15-4696-88d2-5e71b27ec378"
        req.card_token = "11a078c4-3c32-4796-90b1-51ee5517a212"
        req.expire_year = "2044"
        req.expire_month = "07"

        resp = self.payment.update_card(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp.card_token)
        self.assertIsNotNone(resp.card_user_key)
        self.assertEqual("525864", resp.bin_number)
        self.assertEqual("0001", resp.last_four_digits)

    def test_clone_stored_card(self):
        req = CloneCardRequest()
        req.source_card_user_key = "fac377f2-ab15-4696-88d2-5e71b27ec378"
        req.source_card_token = "11a078c4-3c32-4796-90b1-51ee5517a212"
        req.target_merchant_id = 1

        resp = self.payment.clone_card(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp.card_token)
        self.assertIsNotNone(resp.card_user_key)

    def test_search_stored_cards(self):
        req = SearchStoredCardsRequest()
        req.card_alias = "My YKB Card"
        req.card_bank_name = "YAPI VE KREDİ BANKASI A.Ş."
        req.card_brand = "World"
        req.card_association = CardAssociation.MASTER_CARD
        req.card_user_key = "c115ecdf-0afc-4d83-8a1b-719c2af19cbd"
        req.card_token = "d9b19d1a-243c-43dc-a498-add08162df72"
        req.card_type = CardType.CREDIT_CARD

        resp: StoredCardListResponse = self.payment.search_stored_cards(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertTrue(len(resp.items) == 0)

    def test_delete_stored_card(self):
        req = DeleteStoredCardRequest()
        req.card_user_key = "fac377f2-ab15-4696-88d2-5e71b27ec378"
        req.card_token = "11a078c4-3c32-4796-90b1-51ee5517a212"

        self.payment.delete_stored_card(req)

    def test_approve_payment_transactions(self):
        req = ApprovePaymentTransactionsRequest()
        req.is_transactional = True
        req.payment_transaction_ids = [1, 2]

        resp: PaymentTransactionApprovalListResponse = self.payment.approve_payment_transactions(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(2, resp.size)

    def test_disapprove_payment_transactions(self):
        req = DisapprovePaymentTransactionsRequest()
        req.is_transactional = True
        req.payment_transaction_ids = [1, 2]

        resp: PaymentTransactionApprovalListResponse = self.payment.disapprove_payment_transactions(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(2, resp.size)

    def test_create_pre_auth_payment(self):
        items = []

        pi1 = PaymentItem()
        pi1.name = "item 1"
        pi1.external_id = str(uuid.uuid4())
        pi1.price = Decimal("30")
        items.append(pi1)

        pi2 = PaymentItem()
        pi2.name = "item 2"
        pi2.external_id = str(uuid.uuid4())
        pi2.price = Decimal("50")
        items.append(pi2)

        pi3 = PaymentItem()
        pi3.name = "item 3"
        pi3.external_id = str(uuid.uuid4())
        pi3.price = Decimal("20")
        items.append(pi3)

        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "5258640000000001"
        card.expire_year = "2044"
        card.expire_month = "07"
        card.cvc = "000"

        req = CreatePaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.TRY
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.PRE_AUTH
        req.card = card
        req.items = items

        resp = self.payment.create_payment(req)
        print(resp)
        self.assertIsNotNone(resp)

    def test_post_auth_payment(self):
        payment_id = 1
        req = PostAuthPaymentRequest()
        req.paid_price = Decimal("100")

        resp = self.payment.post_auth_payment(payment_id, req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(payment_id, resp.id)
        self.assertEqual(PaymentPhase.POST_AUTH, resp.payment_phase)

    def test_create_multi_currency_payment(self):
        items = []

        pi1 = PaymentItem()
        pi1.name = "item 1"
        pi1.external_id = str(uuid.uuid4())
        pi1.price = Decimal("30")
        items.append(pi1)

        pi2 = PaymentItem()
        pi2.name = "item 2"
        pi2.external_id = str(uuid.uuid4())
        pi2.price = Decimal("50")
        items.append(pi2)

        pi3 = PaymentItem()
        pi3.name = "item 3"
        pi3.external_id = str(uuid.uuid4())
        pi3.price = Decimal("20")
        items.append(pi3)

        card = Card()
        card.card_holder_name = "Haluk Demir"
        card.card_number = "5400010000000004"
        card.expire_year = "2044"
        card.expire_month = "07"
        card.cvc = "000"

        req = CreatePaymentRequest()
        req.price = Decimal("100")
        req.paid_price = Decimal("100")
        req.wallet_price = Decimal("0")
        req.installment = 1
        req.currency = Currency.USD
        req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
        req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
        req.payment_phase = PaymentPhase.AUTH
        req.card = card
        req.items = items

        resp = self.payment.create_payment(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp.id)
        self.assertEqual(Currency.USD, resp.currency)
        self.assertEqual(1, resp.installment)
        self.assertEqual("540001", resp.bin_number)
        self.assertEqual("0004", resp.last_four_digits)
        self.assertTrue(hasattr(resp, "payment_transactions"))
        self.assertEqual(3, len(resp.payment_transactions))

    def test_update_payment_transaction(self):
        req = UpdatePaymentTransactionRequest()
        req.payment_transaction_id = 10
        req.sub_merchant_member_id = 1
        req.sub_merchant_member_price = Decimal("10")

        resp: PaymentTransactionResponse = self.payment.update_payment_transaction(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(req.sub_merchant_member_id, resp.sub_merchant_member_id)
        self.assertEqual(float(req.sub_merchant_member_price), float(resp.sub_merchant_member_price))

    def test_retrieve_multi_payment(self):
        token = "6d7e66b5-9b1c-4c1d-879a-2557b651096e"
        resp: MultiPaymentResponse = self.payment.retrieve_multi_payment(token)
        print(resp)
        self.assertIsNotNone(resp)

    def test_retrieve_provider_card(self):
        req = RetrieveProviderCardRequest()
        req.provider_card_token = "45f12c74-3000-465c-96dc-876850e7dd7a"
        req.provider_card_user_id = "0309ac2d-c5a5-4b4f-a91f-5c444ba07b24"
        req.external_id = "1001"
        req.card_provider = CardProvider.MEX

        resp: StoredCardListResponse = self.payment.retrieve_provider_cards(req)
        print(resp)
        self.assertIsNotNone(resp)

    def test_should_validate_3d_secure_callback_verified(self):
        merchant_key = "merchantThreeDsCallbackKeySndbox"
        params = {
            "hash": "1d3fa1e51fe7c350185c5a7f8c3ff513a991367b08c16a56f4ab9abeb738a1e1",
            "paymentId": "5",
            "conversationData": "conversation-data",
            "conversationId": "conversation-id",
            "status": "SUCCESS",
            "completeStatus": "WAITING",
        }

        is_verified = self.payment.is_3d_secure_callback_verified(merchant_key, params)
        self.assertTrue(is_verified)

    def test_should_validate_3d_secure_callback_verified_even_params_has_nullable_value(self):
        merchant_key = "merchantThreeDsCallbackKeySndbox"
        params = {
            "hash": "a097f0231031a88f2d687b510afca2505ccd2977d6421be4c3784666703f6f25",
            "paymentId": "5",
            "conversationId": "conversation-id",
            "status": "SUCCESS",
            "completeStatus": "WAITING"
        }

        is_verified = self.payment.is_3d_secure_callback_verified(merchant_key, params)
        self.assertTrue(is_verified)

    def test_should_not_validate_3d_secure_callback_when_hashes_are_not_equal(self):
        merchant_key = "merchantThreeDsCallbackKeySndbox"
        params = {
            "hash": "39427942bcaasjaduqabzhdancaASasdhbcxjancakjscace82",
            "paymentId": "5",
            "conversationData": "conversation-data",
            "conversationId": "conversation-id",
            "status": "SUCCESS",
            "completeStatus": "WAITING",
        }

        is_verified = self.payment.is_3d_secure_callback_verified(merchant_key, params)
        self.assertFalse(is_verified)


if __name__ == "__main__":
    unittest.main()
