import os
import unittest

from craftgate import Craftgate, RequestOptions
from craftgate.model import ApmType
from craftgate.request import InitMealVoucherCardTokenizationRequest, MealVoucherCardTokenizationRegenerateRequest, \
    MealVoucherCardTokenizationCompleteRequest
from craftgate.request.dto.meal_voucher_card_tokenization_data import MealVoucherCardTokenizationData


class MealVoucherCardTokenizationSample(unittest.TestCase):
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
        cls.meal_voucher_card_tokenization = Craftgate(options).meal_voucher_card_tokenization()

    def test_init_meal_voucher_card_tokenization(self):
        request = InitMealVoucherCardTokenizationRequest(
            apm_type=ApmType.SETCARD,
            meal_voucher_card_tokenization_data=MealVoucherCardTokenizationData(
                callback_url="https://webhook.site/e806070a-da76-4d02-a67b-54ba9e8332d3"
            )
        )

        response = self.meal_voucher_card_tokenization.init(request)

        print(response.__dict__)
        self.assertIsNotNone(response.session_id)
        self.assertIsNotNone(response)

    def test_regenerate_meal_voucher_card_tokenization(self):
        session_id = "session-id"
        request = MealVoucherCardTokenizationRegenerateRequest(
            meal_voucher_card_tokenization_data=MealVoucherCardTokenizationData(
                callback_url="https://webhook.site/e806070a-da76-4d02-a67b-54ba9e8332d3"
            )
        )

        response = self.meal_voucher_card_tokenization.regenerate(session_id, request)

        print(response.__dict__)
        self.assertIsNotNone(response.session_id)
        self.assertIsNotNone(response)

    def test_complete_meal_voucher_card_tokenization(self):
        session_id = "session-id"
        request = MealVoucherCardTokenizationCompleteRequest(
            validation_code="123456"
        )

        response = self.meal_voucher_card_tokenization.complete(session_id, request)

        print(response.__dict__)
        self.assertIsNotNone(response.session_id)
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
