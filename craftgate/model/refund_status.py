from enum import Enum


class RefundStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    WAITING = "WAITING"
