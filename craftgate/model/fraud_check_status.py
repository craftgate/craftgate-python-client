from enum import Enum


class FraudCheckStatus(str, Enum):
    WAITING = "WAITING"
    NOT_FRAUD = "NOT_FRAUD"
    FRAUD = "FRAUD"
