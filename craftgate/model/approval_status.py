from enum import Enum


class ApprovalStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
