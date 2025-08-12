from enum import Enum


class RefundDestinationType(str, Enum):
    # Deprecated: CARD 
    CARD = "CARD"
    PROVIDER = "PROVIDER"
    WALLET = "WALLET"
