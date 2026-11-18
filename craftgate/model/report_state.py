from enum import Enum


class ReportState(str, Enum):
    DEMANDED = "DEMANDED"
    READY = "READY"
    FAILED = "FAILED"
