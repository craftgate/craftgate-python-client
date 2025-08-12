from enum import Enum

class PosStatus(str, Enum):
    DELETED = "DELETED"
    PASSIVE = "PASSIVE"
    ACTIVE = "ACTIVE"
    REFUND_ONLY = "REFUND_ONLY"
    AUTOPILOT = "AUTOPILOT"