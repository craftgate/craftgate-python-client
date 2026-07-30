# tests/test_idempotency.py
"""Idempotency key tests. No live credentials needed."""
import unittest

from craftgate import RequestOptions
from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.model import FraudCheckStatus, PosStatus
from craftgate.request import (
    CreatePaymentTokenRequest,
    DeleteProductRequest,
    ExpireCheckoutPaymentRequest,
    RemoveValueFromValueListRequest,
    SearchProductsRequest,
    UpdateFraudCheckStatusRequest,
    UpdateMerchantPosStatusRequest,
)
from craftgate.utils.hash_generator import HashGenerator
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder
from craftgate.utils.serializer import serialize_request_body

IDEMPOTENCY_KEY_HEADER_NAME = "x-idempotency-key"
SIGNATURE_HEADER_NAME = "x-signature"
FIXED_RANDOM_KEY = "fixed-random-key"


class FixedRandomAdapter(BaseAdapter):
    """Pins the random key so signatures are comparable across calls."""

    def _generate_random_string(self) -> str:
        return FIXED_RANDOM_KEY


class IdempotencyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = RequestOptions(
            api_key="api-key",
            secret_key="secret-key",
            base_url="https://sandbox-api.craftgate.io"
        )
        cls.adapter = FixedRandomAdapter(cls.options)

    def test_key_is_read_back_from_the_request(self):
        request = CreatePaymentTokenRequest(value="card-value").with_idempotency_key("idempotency-key-1")

        self.assertEqual("idempotency-key-1", request.idempotency_key)
        self.assertEqual("card-value", request.value)

    def test_key_defaults_to_none_and_does_not_leak_between_instances(self):
        with_key = CreatePaymentTokenRequest(value="v").with_idempotency_key("idempotency-key-1")

        self.assertEqual("idempotency-key-1", with_key.idempotency_key)
        self.assertIsNone(CreatePaymentTokenRequest(value="v").idempotency_key)

    def test_key_is_excluded_from_serialized_body(self):
        request = CreatePaymentTokenRequest(value="card-value").with_idempotency_key("idempotency-key-1")

        body = serialize_request_body(request)

        self.assertIn("card-value", body)
        self.assertNotIn("idempotencyKey", body)
        self.assertNotIn("idempotency_key", body)
        self.assertNotIn("idempotency-key-1", body)

    def test_key_is_excluded_from_query_params_of_read_requests(self):
        request = SearchProductsRequest(name="A new Product")
        request.idempotency_key = "idempotency-key-1"

        query = RequestQueryParamsBuilder.build_query_params(request)

        self.assertIn("name=A", query)
        self.assertNotIn("idempotencyKey", query)
        self.assertNotIn("idempotency_key", query)
        self.assertNotIn("idempotency-key-1", query)

    def test_body_request_sends_the_key_as_a_header(self):
        request = CreatePaymentTokenRequest(value="card-value").with_idempotency_key("idempotency-key-1")

        headers = self.adapter._create_headers(request, "/payment/v1/payment-tokens")

        self.assertEqual("idempotency-key-1", headers.get(IDEMPOTENCY_KEY_HEADER_NAME))

    def test_body_request_without_a_key_sends_no_header(self):
        request = CreatePaymentTokenRequest(value="card-value")

        headers = self.adapter._create_headers(request, "/payment/v1/payment-tokens")

        self.assertNotIn(IDEMPOTENCY_KEY_HEADER_NAME, headers)

    def test_bodyless_request_sends_the_key_as_a_header(self):
        request = ExpireCheckoutPaymentRequest(token="token-1").with_idempotency_key("idempotency-key-1")

        headers = self.adapter._create_headers(
            None, "/payment/v1/checkout-payments/token-1", header_options=request)

        self.assertEqual("idempotency-key-1", headers.get(IDEMPOTENCY_KEY_HEADER_NAME))

    def test_bodyless_request_without_a_key_sends_no_header(self):
        request = ExpireCheckoutPaymentRequest(token="token-1")

        headers = self.adapter._create_headers(
            None, "/payment/v1/checkout-payments/token-1", header_options=request)

        self.assertNotIn(IDEMPOTENCY_KEY_HEADER_NAME, headers)

    def test_bodyless_signature_is_unchanged_by_the_key(self):
        """A regression here rejects every delete/approve/cancel call at the API."""
        path = "/payment/v1/checkout-payments/token-1"
        expected = HashGenerator.generate_hash(
            base_url=self.options.base_url,
            api_key=self.options.api_key,
            secret_key=self.options.secret_key,
            random_string=FIXED_RANDOM_KEY,
            request=None,
            path=path,
        )

        wrapper = ExpireCheckoutPaymentRequest(token="token-1").with_idempotency_key("idempotency-key-1")
        with_key = self.adapter._create_headers(None, path, header_options=wrapper)
        without_key = self.adapter._create_headers(None, path)

        self.assertEqual(expected, with_key[SIGNATURE_HEADER_NAME])
        self.assertEqual(expected, without_key[SIGNATURE_HEADER_NAME])

    def test_body_signature_is_unchanged_by_the_key(self):
        path = "/payment/v1/payment-tokens"
        expected = HashGenerator.generate_hash(
            base_url=self.options.base_url,
            api_key=self.options.api_key,
            secret_key=self.options.secret_key,
            random_string=FIXED_RANDOM_KEY,
            request=CreatePaymentTokenRequest(value="card-value"),
            path=path,
        )

        with_key = self.adapter._create_headers(
            CreatePaymentTokenRequest(value="card-value").with_idempotency_key("idempotency-key-1"), path)

        self.assertEqual(expected, with_key[SIGNATURE_HEADER_NAME])

    def test_multi_field_wrappers_carry_their_path_variables(self):
        remove_value = RemoveValueFromValueListRequest(
            list_name="ipList", value_id="value-1").with_idempotency_key("idempotency-key-1")
        pos_status = UpdateMerchantPosStatusRequest(
            merchant_pos_id=1, pos_status=PosStatus.PASSIVE).with_idempotency_key("idempotency-key-2")
        fraud_check = UpdateFraudCheckStatusRequest(
            id=2613, check_status=FraudCheckStatus.FRAUD).with_idempotency_key("idempotency-key-3")

        self.assertEqual(("ipList", "value-1", "idempotency-key-1"),
                         (remove_value.list_name, remove_value.value_id, remove_value.idempotency_key))
        self.assertEqual((1, PosStatus.PASSIVE, "idempotency-key-2"),
                         (pos_status.merchant_pos_id, pos_status.pos_status, pos_status.idempotency_key))
        self.assertEqual((2613, FraudCheckStatus.FRAUD, "idempotency-key-3"),
                         (fraud_check.id, fraud_check.check_status, fraud_check.idempotency_key))

    def test_single_field_wrapper_carries_its_path_variable(self):
        request = DeleteProductRequest(id=42).with_idempotency_key("idempotency-key-1")

        self.assertEqual(42, request.id)
        self.assertEqual("idempotency-key-1", request.idempotency_key)


if __name__ == "__main__":
    unittest.main()
