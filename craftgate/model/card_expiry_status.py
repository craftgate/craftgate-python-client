from enum import Enum

class CardExpiryStatus(str, Enum):
    EXPIRED = "EXPIRED"
    WILL_EXPIRE_NEXT_MONTH = "WILL_EXPIRE_NEXT_MONTH"
    NOT_EXPIRED = "NOT_EXPIRED"