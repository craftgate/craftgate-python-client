from enum import Enum


class SettlementRowItemSubject(str, Enum):
    PAYMENT_TX = "PAYMENT_TX"
    REFUND = "REFUND"
    REFUND_TX = "REFUND_TX"
    MONEY_TRANSFER = "MONEY_TRANSFER"
    WITHDRAW = "WITHDRAW"
