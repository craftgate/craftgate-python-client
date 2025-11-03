from enum import Enum


class AccountOwner(str, Enum):
    MERCHANT = "MERCHANT"
    SUB_MERCHANT_MEMBER = "SUB_MERCHANT_MEMBER"
