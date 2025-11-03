from enum import Enum


class MerchantType(str, Enum):
    MERCHANT = "MERCHANT"
    SUB_MERCHANT_MEMBER = "SUB_MERCHANT_MEMBER"
