from enum import Enum


class FraudAction(str, Enum):
    BLOCK = "BLOCK"
    REVIEW = "REVIEW"
