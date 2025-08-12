from enum import Enum


class RecordType(str, Enum):
    SEND = "SEND"
    RECEIVE = "RECEIVE"
