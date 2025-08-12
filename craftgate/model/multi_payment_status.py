from enum import Enum

class MultiPaymentStatus(str, Enum):
    COMPLETED = "COMPLETED"
    CREATED = "CREATED"