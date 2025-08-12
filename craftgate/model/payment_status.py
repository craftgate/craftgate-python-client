from enum import Enum


class PaymentStatus(str, Enum):
    FAILURE = "FAILURE"
    SUCCESS = "SUCCESS"
    INIT_THREEDS = "INIT_THREEDS"
    CALLBACK_THREEDS = "CALLBACK_THREEDS"
    WAITING = "WAITING"
