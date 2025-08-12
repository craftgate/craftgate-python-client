from enum import Enum

class PosOperationType(str, Enum):
    STANDARD = "STANDARD"
    PROVAUT = "PROVAUT"
    PROVRFN = "PROVRFN"
    PAYMENT = "PAYMENT"
    REFUND = "REFUND"
    INQUIRY = "INQUIRY"