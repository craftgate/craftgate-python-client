from enum import Enum


class RefundType(str, Enum):
    CANCEL = "CANCEL"
    REFUND = "REFUND"
