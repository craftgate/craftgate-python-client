import base64
import hmac
from hashlib import sha256
from typing import Optional

from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.model.webhook_data import WebhookData
from craftgate.request_options import RequestOptions


class HookAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(HookAdapter, self).__init__(request_options)

    def is_webhook_verified(self, merchant_hook_key: str, incoming_signature: str, webhook_data: WebhookData) -> bool:
        if merchant_hook_key is None or incoming_signature is None or webhook_data is None:
            return False

        data = "{}{}{}{}".format(
            webhook_data.event_type,
            webhook_data.event_timestamp,
            webhook_data.status,
            webhook_data.payload_id
        )

        signature = self._generate_hash(merchant_hook_key, data)
        return incoming_signature == signature

    def _generate_hash(self, merchant_hook_key: str, data: str) -> Optional[str]:
        try:
            key_bytes = merchant_hook_key.encode("utf-8")
            data_bytes = data.encode("utf-8")
            digest = hmac.new(key_bytes, data_bytes, sha256).digest()
            return base64.b64encode(digest).decode("utf-8")
        except Exception:
            return None
