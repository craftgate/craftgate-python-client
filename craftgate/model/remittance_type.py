from enum import Enum


class RemittanceType(str, Enum):
    SEND = "SEND"
    RECEIVE = "RECEIVE"
