from typing import Optional
from datetime import datetime

from craftgate.model.webhook_event_type import WebhookEventType
from craftgate.model.webhook_status import WebhookStatus


class WebhookData(object):
    def __init__(
            self,
            event_type: Optional[WebhookEventType] = None,
            event_time: Optional[datetime] = None,
            event_timestamp: Optional[int] = None,
            status: Optional[WebhookStatus] = None,
            payload_id: Optional[str] = None
    ) -> None:
        self.event_type = event_type
        self.event_time = event_time
        self.event_timestamp = event_timestamp
        self.status = status
        self.payload_id = payload_id
