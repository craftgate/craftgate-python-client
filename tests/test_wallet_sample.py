# tests/test_wallet_sample.py
import os
import unittest
from decimal import Decimal

from craftgate import Craftgate, RequestOptions
from craftgate.model import Currency, RefundStatus, RemittanceReasonType, RemittanceType, Status, \
    TransactionPayoutStatus, WalletTransactionRefundCardTransactionType
from craftgate.request import CreateRemittanceRequest, CreateWalletRequest, CreateWithdrawRequest, \
    RefundWalletTransactionToCardRequest, ResetMerchantMemberWalletBalanceRequest, SearchWalletTransactionsRequest, \
    SearchWithdrawsRequest, UpdateWalletRequest


class WalletSample(unittest.TestCase):
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
        cls.wallet = Craftgate(options).wallet()

    def test_retrieve_member_wallet(self):
        member_id = 116212
        response = self.wallet.retrieve_member_wallet(member_id)
        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertIsNotNone(response.created_date)
        self.assertIsNotNone(response.amount)
        self.assertIsNotNone(response.withdrawal_amount)
        self.assertEqual(member_id, response.member_id)
        self.assertEqual(Currency.TRY, response.currency)

    def test_search_wallet_transactions(self):
        wallet_id = 96749
        request = SearchWalletTransactionsRequest()
        response = self.wallet.search_wallet_transactions(wallet_id, request)
        print(vars(response))
        self.assertTrue(len(response.items) > 0)

    def test_send_remittance(self):
        member_id = 116212
        price = Decimal("50")
        request = CreateRemittanceRequest(
            member_id=member_id,
            price=price,
            description="Loyalty send to memberId{}".format(member_id),
            remittance_reason_type=RemittanceReasonType.REDEEM_ONLY_LOYALTY
        )
        response = self.wallet.send_remittance(request)
        print(vars(response))
        self.assertIsNotNone(response)
        self.assertEqual(request.member_id, response.member_id)
        self.assertEqual(request.price, response.price)
        self.assertEqual(request.description, response.description)
        self.assertEqual(RemittanceType.SEND, response.remittance_type)
        self.assertEqual(RemittanceReasonType.REDEEM_ONLY_LOYALTY, response.remittance_reason_type)

    def test_receive_remittance(self):
        member_id = 116212
        price = Decimal("50")
        request = CreateRemittanceRequest(
            member_id=member_id,
            price=price,
            description="Loyalty received from memberId{}".format(member_id),
            remittance_reason_type=RemittanceReasonType.REDEEM_ONLY_LOYALTY
        )
        response = self.wallet.receive_remittance(request)
        print(vars(response))
        self.assertIsNotNone(response)
        self.assertEqual(request.member_id, response.member_id)
        self.assertEqual(request.price, response.price)
        self.assertEqual(request.description, response.description)
        self.assertEqual(RemittanceType.RECEIVE, response.remittance_type)
        self.assertEqual(RemittanceReasonType.REDEEM_ONLY_LOYALTY, response.remittance_reason_type)

    def test_retrieve_remittance(self):
        remittance_id = 96386
        response = self.wallet.retrieve_remittance(remittance_id)
        print(vars(response))
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.price)
        self.assertIsNotNone(response.member_id)
        self.assertIsNotNone(response.description)
        self.assertEqual(RemittanceType.SEND, response.remittance_type)
        self.assertEqual(RemittanceReasonType.REDEEM_ONLY_LOYALTY, response.remittance_reason_type)

    def test_retrieve_merchant_member_wallet(self):
        response = self.wallet.retrieve_merchant_member_wallet()
        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertIsNotNone(response.created_date)
        self.assertIsNotNone(response.member_id)
        self.assertIsNotNone(response.amount)
        self.assertEqual(Currency.TRY, response.currency)

    def test_reset_merchant_member_wallet_balance(self):
        request = ResetMerchantMemberWalletBalanceRequest(
            wallet_amount=Decimal("-5")
        )
        response = self.wallet.reset_merchant_member_wallet_balance(request)
        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertIsNotNone(response.created_date)
        self.assertIsNotNone(response.member_id)
        self.assertEqual(Decimal("0"), response.amount)
        self.assertEqual(Currency.TRY, response.currency)

    def test_retrieve_refundable_amount_of_wallet_transaction(self):
        wallet_transaction_id = 236377
        response = self.wallet.retrieve_refundable_amount_of_wallet_transaction(wallet_transaction_id)
        print(vars(response))
        self.assertTrue(response.refundable_amount > 0)

    def test_refund_wallet_transaction_to_card(self):
        wallet_transaction_id = 236372
        request = RefundWalletTransactionToCardRequest(
            refund_price=Decimal("10")
        )
        response = self.wallet.refund_wallet_transaction(wallet_transaction_id, request)
        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertIsNone(response.payment_error)
        self.assertEqual(RefundStatus.SUCCESS, response.refund_status)
        self.assertEqual(WalletTransactionRefundCardTransactionType.PAYMENT, response.transaction_type)
        self.assertEqual(wallet_transaction_id, response.wallet_transaction_id)
        self.assertEqual(request.refund_price, response.refund_price)

    def test_retrieve_refund_wallet_transactions_to_card(self):
        wallet_transaction_id = 236372
        response = self.wallet.retrieve_refund_wallet_transactions(wallet_transaction_id)
        print(vars(response))
        self.assertIsNotNone(response.items)
        self.assertTrue(len(response.items) > 0)

    def test_create_withdraw(self):
        request = CreateWithdrawRequest(
            member_id=116212,
            price=Decimal("5"),
            description="Hakediş Çekme Talebi",
            currency=Currency.TRY
        )
        response = self.wallet.create_withdraw(request)
        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertIsNone(response.payout_id)
        self.assertIsNotNone(response.created_date)
        self.assertEqual(Status.ACTIVE, response.status)
        self.assertEqual(request.price, response.price)
        self.assertEqual(request.currency, response.currency)
        self.assertEqual(request.description, response.description)
        self.assertEqual(TransactionPayoutStatus.WAITING_FOR_PAYOUT, response.payout_status)
        self.assertEqual(request.member_id, response.member_id)

    def test_cancel_withdraw(self):
        withdraw_id = 1136
        response = self.wallet.cancel_withdraw(withdraw_id)
        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertIsNotNone(response.created_date)
        self.assertEqual(Status.ACTIVE, response.status)
        self.assertEqual(TransactionPayoutStatus.CANCELLED, response.payout_status)

    def test_retrieve_withdraw(self):
        withdraw_id = 1136
        response = self.wallet.retrieve_withdraw(withdraw_id)
        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertIsNotNone(response.created_date)
        self.assertEqual(Status.ACTIVE, response.status)
        self.assertEqual(Currency.TRY, response.currency)
        self.assertEqual(TransactionPayoutStatus.WAITING_FOR_PAYOUT, response.payout_status)

    def test_search_withdraws(self):
        request = SearchWithdrawsRequest(
            payout_status=TransactionPayoutStatus.WAITING_FOR_PAYOUT,
            min_withdraw_price=Decimal("5"),
            max_withdraw_price=Decimal("1000")
        )
        response = self.wallet.search_withdraws(request)
        print(vars(response))
        self.assertIsNotNone(response.page)
        self.assertIsNotNone(response.size)
        self.assertIsNotNone(response.total_size)
        self.assertTrue(len(response.items) > 0)

    def test_create_member_wallet(self):
        member_id = 116212
        request = CreateWalletRequest(
            currency=Currency.TRY,
            negative_amount_limit=Decimal("0")
        )
        response = self.wallet.create_wallet(member_id, request)
        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertEqual(Currency.TRY, response.currency)

    def test_update_member_wallet(self):
        member_id = 116212
        wallet_id = 96749
        request = UpdateWalletRequest(
            negative_amount_limit=Decimal("-10")
        )
        response = self.wallet.update_wallet(member_id, wallet_id, request)
        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertEqual(Decimal("-10"), response.negative_amount_limit)


if __name__ == "__main__":
    unittest.main()
