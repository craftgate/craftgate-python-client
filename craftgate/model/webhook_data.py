from typing import Optional
from datetime import datetime

from craftgate.model.webhook_event_type import WebhookEventType
from craftgate.model.webhook_status import WebhookStatus


class WebhookData(object):
    def __init__(
        self,
        event_type=None,           # type: Optional[WebhookEventType]
        event_time=None,           # type: Optional[datetime]
        event_timestamp=None,      # type: Optional[int]
        status=None,               # type: Optional[WebhookStatus]
        payload_id=None            # type: Optional[str]
    ):
        self.event_type = event_type
        self.event_time = event_time
        self.event_timestamp = event_timestamp
        self.status = status
        self.payload_id = payload_id