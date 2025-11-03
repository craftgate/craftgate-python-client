from enum import Enum


class MasterpassValidationType(str, Enum):
    NONE = "NONE"
    OTP = "OTP"
    THREE_DS = "THREE_DS"
