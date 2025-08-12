from enum import Enum


class CardType(str, Enum):
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"
    PREPAID_CARD = "PREPAID_CARD"
