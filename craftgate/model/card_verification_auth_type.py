from enum import Enum


class CardVerificationAuthType(str, Enum):
    NON_THREE_DS = "NON_THREE_DS"
    THREE_DS = "THREE_DS"
    NONE = "NONE"
