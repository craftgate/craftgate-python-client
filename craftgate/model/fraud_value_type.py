from enum import Enum

class FraudValueType(str, Enum):
    CARD = "CARD"
    IP = "IP"
    PHONE_NUMBER = "PHONE_NUMBER"
    EMAIL = "EMAIL"
    OTHER = "OTHER"
