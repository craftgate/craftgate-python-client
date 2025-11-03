# tests/test_pay_by_link_sample.py
import os
import unittest
from datetime import datetime, timedelta
from decimal import Decimal

from craftgate import Craftgate, RequestOptions
from craftgate.model import Currency, Status
from craftgate.request import CreateProductRequest, SearchProductsRequest, UpdateProductRequest


class PayByLinkSample(unittest.TestCase):
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
        cls.pay_by_link = Craftgate(options).pay_by_link()

    def test_create_product(self):
        expires_at = (datetime.now() + timedelta(days=5)).replace(microsecond=0)

        request = CreateProductRequest(
            name="A new Product",
            channel="API",
            price=Decimal("10"),
            currency=Currency.TRY,
            conversation_id="my-conversationId",
            external_id="my-externalId",
            expires_at=expires_at,
            enabled_installments={1, 2, 3, 6}
        )

        response = self.pay_by_link.create_product(request)

        print(response)

        self.assertIsNotNone(response)
        self.assertEqual(response.status, Status.ACTIVE)
        self.assertEqual(response.name, request.name)
        self.assertEqual(response.price, request.price)
        self.assertEqual(response.channel, request.channel)
        self.assertEqual(response.currency, request.currency)
        self.assertEqual(set(response.enabled_installments), set(request.enabled_installments))
        self.assertIsNotNone(response.url)
        self.assertIsNotNone(response.token)
        self.assertEqual(response.expires_at, expires_at)

    def test_update_product(self):
        product_id = 6807
        request = UpdateProductRequest(
            status=Status.ACTIVE,
            name="A new Product - version 2",
            channel="API",
            price=Decimal("10"),
            currency=Currency.TRY,
            enabled_installments={1, 2, 3, 6}
        )

        response = self.pay_by_link.update_product(product_id, request)

        print(response)

        self.assertIsNotNone(response)
        self.assertEqual(response.status, Status.ACTIVE)
        self.assertEqual(response.name, request.name)
        self.assertEqual(response.price, request.price)
        self.assertEqual(response.channel, request.channel)
        self.assertEqual(response.currency, request.currency)
        self.assertEqual(set(response.enabled_installments), set(request.enabled_installments))
        self.assertIsNotNone(response.url)
        self.assertIsNotNone(response.token)

    def test_retrieve_product(self):
        product_id = 6807
        response = self.pay_by_link.retrieve_product(product_id)

        print(response)

        self.assertIsNotNone(response)
        self.assertEqual(response.id, product_id)
        self.assertIsNotNone(response.name)
        self.assertIsNotNone(response.price)
        self.assertIsNotNone(response.url)
        self.assertIsNotNone(response.token)

    def test_delete_product(self):
        product_id = 6807
        self.pay_by_link.delete_product(product_id)
        self.assertTrue(True)

    def test_search_products(self):
        request = SearchProductsRequest(
            name="A new Product",
            channel="API",
            currency=Currency.TRY
        )

        response = self.pay_by_link.search_products(request)

        print(response)
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
