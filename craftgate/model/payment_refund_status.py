from enum import Enum


class PaymentRefundStatus(str, Enum):
    NO_REFUND = "NO_REFUND"
    NOT_REFUNDED = "NOT_REFUNDED"
    PARTIAL_REFUNDED = "PARTIAL_REFUNDED"
    FULLY_REFUNDED = "FULLY_REFUNDED"
