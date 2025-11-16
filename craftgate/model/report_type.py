from enum import Enum


class ReportType(str, Enum):
    TRANSACTION = "TRANSACTION"
    PAYMENT = "PAYMENT"
