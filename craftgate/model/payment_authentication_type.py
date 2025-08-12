from enum import Enum

class PaymentAuthenticationType(str, Enum):
    THREE_DS = "THREE_DS"
    NON_THREE_DS = "NON_THREE_DS"
    BKM_EXPRESS = "BKM_EXPRESS"