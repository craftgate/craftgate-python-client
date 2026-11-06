from enum import Enum


class PayoutApprovalStatus(str, Enum):
    WAITING = "WAITING"
    APPROVED = "APPROVED"
