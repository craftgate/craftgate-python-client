from enum import Enum


class TransactionStatus(str, Enum):
    WAITING_FOR_APPROVAL = "WAITING_FOR_APPROVAL"
    APPROVED = "APPROVED"
    PAYOUT_STARTED = "PAYOUT_STARTED"
