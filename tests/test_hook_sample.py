# tests/test_hook_sample.py
import os
import unittest
from datetime import datetime

from craftgate import Craftgate, RequestOptions
from craftgate.model import WebhookData, WebhookEventType, WebhookStatus


class HookSample(unittest.TestCase):
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
        cls.hook = Craftgate(options).hook()

    def test_should_verify_webhook_signature(self):
        merchant_hook_key = "Aoh7tReTybO6wOjBmOJFFsOR53SBojEp"
        incoming_signature = "0wRB5XqWJxwwPbn5Z9TcbHh8EGYFufSYTsRMB74N094="
        webhook_data = WebhookData(
            event_type=WebhookEventType.API_VERIFY_AND_AUTH,
            event_time=datetime(2025, 7, 21, 16, 40, 21, 395655),
            event_timestamp=1661521221,
            status=WebhookStatus.SUCCESS,
            payload_id="584"
        )
        is_verified = self.hook.is_webhook_verified(merchant_hook_key, incoming_signature, webhook_data)
        self.assertTrue(is_verified)

    def test_should_not_verify_webhook_signature(self):
        merchant_hook_key = "Aoh7tReTybO6wOjBmOJFFsOR53SBojEp"
        incoming_signature = "Bsa498wcnaasd4bhx8anxıxcsdnxanalkdjcahxhd"
        webhook_data = WebhookData(
            event_type=WebhookEventType.API_VERIFY_AND_AUTH,
            event_time=datetime(2025, 7, 26, 16, 40, 21, 395655),
            event_timestamp=1661521221,
            status=WebhookStatus.SUCCESS,
            payload_id="584"
        )
        is_verified = self.hook.is_webhook_verified(merchant_hook_key, incoming_signature, webhook_data)
        self.assertFalse(is_verified)


if __name__ == "__main__":
    unittest.main()
