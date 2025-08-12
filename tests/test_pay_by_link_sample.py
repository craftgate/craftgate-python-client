# tests/test_pay_by_link_sample.py
import os
import unittest
from decimal import Decimal

from craftgate.adapter.pay_by_link_adapter import PayByLinkAdapter
from craftgate.model.currency import Currency
from craftgate.model.status import Status
from craftgate.request.create_product_request import CreateProductRequest
from craftgate.request.search_products_request import SearchProductsRequest
from craftgate.request.update_product_request import UpdateProductRequest
from craftgate.request_options import RequestOptions


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
        cls.adapter = PayByLinkAdapter(options)

    def test_create_product(self):
        request = CreateProductRequest(
            name="A new Product",
            channel="API",
            price=Decimal("10"),
            currency=Currency.TRY,
            conversation_id="my-conversationId",
            external_id="my-externalId",
            enabled_installments={1, 2, 3, 6}
        )

        response = self.adapter.create_product(request)

        print(vars(response))
        self.assertIsNotNone(response)
        self.assertEqual(response.status, Status.ACTIVE)
        self.assertEqual(response.name, request.name)
        self.assertEqual(response.price, request.price)
        self.assertEqual(response.channel, request.channel)
        self.assertEqual(response.currency, request.currency)
        self.assertEqual(set(response.enabled_installments), set(request.enabled_installments))
        self.assertIsNotNone(response.url)
        self.assertIsNotNone(response.token)

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

        response = self.adapter.update_product(product_id, request)

        print(vars(response))
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
        response = self.adapter.retrieve_product(product_id)

        print(vars(response))

        self.assertIsNotNone(response)
        self.assertEqual(response.id, product_id)
        self.assertIsNotNone(response.name)
        self.assertIsNotNone(response.price)
        self.assertIsNotNone(response.url)
        self.assertIsNotNone(response.token)

    def test_delete_product(self):
        product_id = 6807
        self.adapter.delete_product(product_id)
        self.assertTrue(True)

    def test_search_products(self):
        request = SearchProductsRequest(
            name="A new Product",
            channel="API",
            currency=Currency.TRY
        )

        response = self.adapter.search_products(request)

        print(vars(response))

        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
