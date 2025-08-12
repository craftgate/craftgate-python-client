# tests/test_payment_reporting_sample.py
import os
import unittest
from datetime import datetime, timedelta
from decimal import Decimal

from craftgate.adapter.payment_reporting_adapter import PaymentReportingAdapter
from craftgate.model.currency import Currency
from craftgate.model.payment_status import PaymentStatus
from craftgate.model.payment_type import PaymentType
from craftgate.model.refund_status import RefundStatus
from craftgate.request.search_payment_refunds_request import SearchPaymentRefundsRequest
from craftgate.request.search_payment_transaction_refunds_request import SearchPaymentTransactionRefundsRequest
from craftgate.request.search_payments_request import SearchPaymentsRequest
from craftgate.request_options import RequestOptions


class PaymentReportingSample(unittest.TestCase):
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
        cls.adapter = PaymentReportingAdapter(options)

    def test_search_payments(self):
        now = datetime.now()
        request = SearchPaymentsRequest(
            page=0,
            size=10,
            payment_id=1289316,
            payment_transaction_id=1244082,
            buyer_member_id=116210,
            conversation_id="conversationId",
            external_id="externalId",
            order_id="orderId",
            payment_type=PaymentType.CARD_PAYMENT,
            payment_status=PaymentStatus.SUCCESS,
            bin_number="123456",
            last_four_digits="1234",
            currency=Currency.TRY,
            min_paid_price=Decimal("1"),
            max_paid_price=Decimal("100"),
            installment=1,
            is_three_ds=False,
            min_created_date=now - timedelta(days=30),
            max_created_date=now
        )
        response = self.adapter.search_payments(request)
        print(vars(response))
        self.assertTrue(len(response.items) > 0)

    def test_retrieve_payment(self):
        payment_id = 1289316
        response = self.adapter.retrieve_payment(payment_id)
        print(vars(response))
        self.assertEqual(payment_id, response.id)
        self.assertIsNotNone(response.price)
        self.assertIsNotNone(response.paid_price)
        self.assertIsNotNone(response.payment_type)
        self.assertIsNotNone(response.payment_status)
        self.assertIsNotNone(response.refundable_price)

    def test_retrieve_payment_transactions(self):
        payment_id = 1289316
        response = self.adapter.retrieve_payment_transactions(payment_id)
        print(vars(response))
        self.assertTrue(len(response.items) > 0)

    def test_retrieve_payment_refunds(self):
        payment_id = 1289311
        response = self.adapter.retrieve_payment_refunds(payment_id)
        print(vars(response))
        self.assertTrue(len(response.items) > 0)

    def test_retrieve_payment_transaction_refunds(self):
        payment_id = 1289311
        payment_transaction_id = 1244069
        response = self.adapter.retrieve_payment_transaction_refunds(payment_id, payment_transaction_id)
        print(vars(response))
        self.assertTrue(len(response.items) > 0)

    def test_search_payment_refunds(self):
        now = datetime.now()
        request = SearchPaymentRefundsRequest(
            page=0,
            size=10,
            id=1,
            payment_id=100,
            buyer_member_id=1,
            conversation_id="conversationId",
            status=RefundStatus.SUCCESS,
            currency=Currency.TRY,
            min_refund_price=Decimal("1"),
            max_refund_price=Decimal("100"),
            min_created_date=now - timedelta(days=30),
            max_created_date=now
        )
        response = self.adapter.search_payment_refunds(request)
        print(vars(response))
        self.assertTrue(len(response.items) > 0)

    def test_search_payment_transaction_refunds(self):
        now = datetime.now()
        request = SearchPaymentTransactionRefundsRequest(
            page=0,
            size=10,
            id=1,
            payment_id=100,
            payment_transaction_id=1000,
            buyer_member_id=1,
            conversation_id="conversationId",
            status=RefundStatus.SUCCESS,
            currency=Currency.TRY,
            min_refund_price=Decimal("1"),
            max_refund_price=Decimal("100"),
            is_after_settlement=False,
            min_created_date=now - timedelta(days=30),
            max_created_date=now
        )
        response = self.adapter.search_payment_transaction_refunds(request)
        print(vars(response))
        self.assertTrue(len(response.items) > 0)


if __name__ == "__main__":
    unittest.main()
