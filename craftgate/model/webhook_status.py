from enum import Enum


class WebhookStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
