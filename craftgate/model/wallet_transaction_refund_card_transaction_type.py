from enum import Enum


class WalletTransactionRefundCardTransactionType(str, Enum):
    PAYMENT = "PAYMENT"
    PAYMENT_TX = "PAYMENT_TX"
    WALLET_TX = "WALLET_TX"
