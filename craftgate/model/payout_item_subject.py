from enum import Enum


class PayoutItemSubject(str, Enum):
    PAYMENT_TX = "PAYMENT_TX"
    REFUND = "REFUND"
    REFUND_TX = "REFUND_TX"
