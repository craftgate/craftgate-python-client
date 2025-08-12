from enum import Enum


class SettlementType(str, Enum):
    SETTLEMENT = "SETTLEMENT"
    BOUNCED_SETTLEMENT = "BOUNCED_SETTLEMENT"
    WITHDRAW = "WITHDRAW"
