from enum import Enum


class CardVerifyStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    THREE_DS_PENDING = "THREE_DS_PENDING"
