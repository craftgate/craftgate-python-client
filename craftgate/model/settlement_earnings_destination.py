from enum import Enum


class SettlementEarningsDestination(str, Enum):
    IBAN = "IBAN"
    WALLET = "WALLET"
    NONE = "NONE"
