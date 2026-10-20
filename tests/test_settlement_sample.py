# tests/test_settlement_sample.py
import os
import unittest

from craftgate import Craftgate, RequestOptions
from craftgate.request import CreateInstantWalletSettlementRequest


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


if __name__ == "__main__":
    unittest.main()
