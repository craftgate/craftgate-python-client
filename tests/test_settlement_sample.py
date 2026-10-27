# tests/test_settlement_sample.py
import os
import unittest
from decimal import Decimal

from craftgate import Craftgate, RequestOptions
from craftgate.model import AccountOwner, Currency, MerchantType, PayoutAccountType
from craftgate.request import ApprovePaymentTransactionsRequest, CreateInstantWalletSettlementRequest, \
    CreatePayoutAccountRequest, DeletePayoutAccountRequest, DisapprovePaymentTransactionsRequest, \
    SearchPayoutAccountRequest, UpdatePaymentTransactionRequest, UpdatePayoutAccountRequest
from craftgate.response import PaymentTransactionApprovalListResponse, PaymentTxPayoutResponse


class SettlementSample(unittest.TestCase):
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
        cls.settlement = Craftgate(options).settlement()

    def test_create_instant_wallet_settlement(self):
        request = CreateInstantWalletSettlementRequest()
        response = self.settlement.create_instant_wallet_settlement(request)

        print(response)
        self.assertIsNotNone(response.settlement_result_status)

    def test_create_merchant_payout_account(self):
        request = CreatePayoutAccountRequest(
            account_owner=AccountOwner.MERCHANT,
            currency=Currency.USD,
            type=PayoutAccountType.WISE,
            external_account_id="wiseRecipientId"
        )
        response = self.settlement.create_payout_account(request)

        print(response)
        self.assertIsNotNone(response.id)

    def test_create_sub_merchant_payout_account(self):
        request = CreatePayoutAccountRequest(
            account_owner=AccountOwner.SUB_MERCHANT_MEMBER,
            sub_merchant_member_id=1,
            currency=Currency.USD,
            type=PayoutAccountType.WISE,
            external_account_id="wiseRecipientId"
        )
        response = self.settlement.create_payout_account(request)

        print(response)
        self.assertIsNotNone(response.id)

    def test_update_payout_account(self):
        request = UpdatePayoutAccountRequest(
            type=PayoutAccountType.WISE,
            external_account_id="wiseRecipientId2"
        )
        self.settlement.update_payout_account(11, request)
        self.assertTrue(True)

    def test_search_payout_account(self):
        request = SearchPayoutAccountRequest(
            account_owner=AccountOwner.MERCHANT,
            currency=Currency.USD,
            page=0,
            size=10
        )
        response = self.settlement.search_payout_account(request)

        print(response)
        self.assertIsNotNone(response.items)

    def test_delete_payout_account(self):
        self.settlement.delete_payout_account(DeletePayoutAccountRequest(id=10))
        self.assertTrue(True)

    def test_approve_payment_transactions(self):
        req = ApprovePaymentTransactionsRequest()
        req.is_transactional = True
        req.payment_transaction_ids = [1, 2]

        resp: PaymentTransactionApprovalListResponse = self.settlement.approve_payment_transactions(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(2, resp.size)

    def test_disapprove_payment_transactions(self):
        req = DisapprovePaymentTransactionsRequest()
        req.is_transactional = True
        req.payment_transaction_ids = [1, 2]

        resp: PaymentTransactionApprovalListResponse = self.settlement.disapprove_payment_transactions(req)
        print(resp)
        self.assertIsNotNone(resp)
        self.assertEqual(2, resp.size)

    def test_update_payment_transaction(self):
        req = UpdatePaymentTransactionRequest()
        req.payment_transaction_id = 10
        req.sub_merchant_member_id = 1
        req.sub_merchant_member_price = Decimal("10")

        resp: PaymentTxPayoutResponse = self.settlement.update_payment_transaction(req)
        print(resp)
        self.assertEqual(req.payment_transaction_id, resp.payment_transaction_id)
        self.assertTrue(any(
            item.merchant_type == MerchantType.SUB_MERCHANT_MEMBER and item.merchant_id == req.sub_merchant_member_id
            for item in resp.payout_items
        ))


if __name__ == "__main__":
    unittest.main()
