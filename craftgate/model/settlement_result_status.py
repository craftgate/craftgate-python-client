from enum import Enum

class SettlementResultStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    NO_RECORD_FOUND = "NO_RECORD_FOUND"
