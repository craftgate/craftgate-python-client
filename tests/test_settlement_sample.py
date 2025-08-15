# tests/test_settlement_sample.py
import os
import unittest

from craftgate import Craftgate, RequestOptions
from craftgate.model import AccountOwner, Currency, PayoutAccountType
from craftgate.request import CreateInstantWalletSettlementRequest, CreatePayoutAccountRequest, \
    SearchPayoutAccountRequest, UpdatePayoutAccountRequest


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

        print(vars(response))
        self.assertIsNotNone(response.settlement_result_status)

    def test_create_merchant_payout_account(self):
        request = CreatePayoutAccountRequest(
            account_owner=AccountOwner.MERCHANT,
            currency=Currency.USD,
            type=PayoutAccountType.WISE,
            external_account_id="wiseRecipientId"
        )
        response = self.settlement.create_payout_account(request)

        print(vars(response))
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

        print(vars(response))
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

        print(vars(response))
        self.assertIsNotNone(response.items)

    def test_delete_payout_account(self):
        self.settlement.delete_payout_account(10)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
