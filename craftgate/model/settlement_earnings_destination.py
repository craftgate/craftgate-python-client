from enum import Enum

class SettlementEarningsDestination(str, Enum):
    IBAN = "IBAN"
    WALLET = "WALLET"
    CROSS_BORDER = "CROSS_BORDER"
    NONE = "NONE"