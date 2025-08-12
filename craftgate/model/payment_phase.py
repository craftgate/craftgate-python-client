from enum import Enum


class PaymentPhase(str, Enum):
    AUTH = "AUTH"
    PRE_AUTH = "PRE_AUTH"
    POST_AUTH = "POST_AUTH"
