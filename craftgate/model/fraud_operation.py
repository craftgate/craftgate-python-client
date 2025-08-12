from enum import Enum


class FraudOperation(str, Enum):
    PAYMENT = "PAYMENT"
    LOYALTY = "LOYALTY"
