from enum import Enum

class SettlementSource(str, Enum):
    COLLECTION = "COLLECTION"
    WITHDRAW = "WITHDRAW"
    BOUNCED = "BOUNCED"
