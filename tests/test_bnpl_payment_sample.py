# tests/test_bnpl_payment_sample.py
import os
import unittest
import uuid
from decimal import Decimal

from craftgate import Craftgate, RequestOptions
from craftgate.model import ApmType, BnplCartItemType, Currency, PaymentGroup
from craftgate.request import BnplPaymentOfferRequest, InitBnplPaymentRequest
from craftgate.request.dto import BnplPaymentCartItem, PaymentItem


class BnplPaymentSample(unittest.TestCase):
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

    def test_retrieve_bank_offer(self):
        items = [
            BnplPaymentCartItem(
                id="1234",
                name="item 1",
                brand_name="Iphone",
                type=BnplCartItemType.MOBILE_PHONE_PRICE_BELOW_REGULATION_LIMIT,
                unit_price=Decimal("3000"),
                quantity=2
            ),
            BnplPaymentCartItem(
                id="123",
                name="item 2",
                brand_name="Samsung",
                type=BnplCartItemType.OTHER,
                unit_price=Decimal("4000"),
                quantity=1
            )
        ]

        request = BnplPaymentOfferRequest(
            apm_type=ApmType.MASLAK,
            price=Decimal("10000"),
            currency=Currency.TRY,
            apm_order_id=str(uuid.uuid4()),
            items=items
        )

        response = self.payment.retrieve_bnpl_payment_offers(request)
        print(response)

        self.assertIsNotNone(response.offer_id)
        self.assertIsNotNone(response.bank_offers)
        self.assertTrue(len(response.bank_offers) > 0)
        self.assertIsNotNone(response.bank_offers[0])

    def test_init_bnpl_payment(self):
        price = Decimal("10000")
        payment_items = [
            PaymentItem(name="item-1", external_id="38983903", price=Decimal("3000")),
            PaymentItem(name="item-2", external_id="92983294", price=Decimal("7000"))
        ]

        cart_items = [
            BnplPaymentCartItem(
                id="200",
                name="Test Elektronik 2",
                brand_name="iphone",
                type=BnplCartItemType.OTHER,
                unit_price=Decimal("7000"),
                quantity=2
            ),
            BnplPaymentCartItem(
                id="100",
                name="Test Elektronik 1",
                brand_name="Samsung",
                type=BnplCartItemType.MOBILE_PHONE_PRICE_ABOVE_REGULATION_LIMIT,
                unit_price=Decimal("3000"),
                quantity=1
            )
        ]

        request = InitBnplPaymentRequest(
            price=price,
            paid_price=price,
            currency=Currency.TRY,
            apm_type=ApmType.MASLAK,
            apm_order_id=str(uuid.uuid4()),
            payment_group=PaymentGroup.PRODUCT,
            conversation_id="29393-mXld92ko3",
            external_id="external_id-345",
            callback_url="callback",
            items=payment_items,
            bank_code="103",
            cart_items=cart_items
        )

        response = self.payment.init_bnpl_payment(request)
        print(response)

        self.assertIsNotNone(response.redirect_url)

    def test_init_tom_finance_bnpl_payment(self):
        price = Decimal("100")
        additional_params = {
            "buyerName": "John Doe",
            "buyerPhoneNumber": "5551112233"
        }

        payment_items = [
            PaymentItem(name="item-1", external_id="externalId", price=Decimal("100"))
        ]

        cart_items = [
            BnplPaymentCartItem(
                id="26020874",
                name="Item 1",
                brand_name="26010303",
                type=BnplCartItemType.OTHER,
                unit_price=Decimal("100"),
                quantity=1
            )
        ]

        request = InitBnplPaymentRequest(
            price=price,
            paid_price=price,
            currency=Currency.TRY,
            apm_type=ApmType.TOM_FINANCE,
            apm_order_id=str(uuid.uuid4()),
            payment_group=PaymentGroup.PRODUCT,
            conversation_id="conversationId",
            external_id="externalId",
            callback_url="https://www.your-website.com/bnpl-callback",
            items=payment_items,
            cart_items=cart_items,
            additional_params=additional_params
        )

        response = self.payment.init_bnpl_payment(request)
        print(response)

        self.assertIsNotNone(response.redirect_url)

    def test_approve_bnpl_payment(self):
        payment_id = 1

        response = self.payment.approve_bnpl_payment(payment_id)
        print(response)

        self.assertIsNotNone(response.id)

    def test_verify_bnpl_payment(self):
        payment_id = 1

        response = self.payment.verify_bnpl_payment(payment_id)
        print(response)

        self.assertIsNotNone(response.payment_status)


if __name__ == "__main__":
    unittest.main()
