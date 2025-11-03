from enum import Enum


class FileStatus(str, Enum):
    CREATED = "CREATED"
    UPLOADED = "UPLOADED"
    APPROVED = "APPROVED"
