from enum import Enum


class PosApmPaymentProvider(str, Enum):
    YKB_WORLD_PAY = "YKB_WORLD_PAY"
    YKB_WORLD_PAY_SHOPPING_LOAN = "YKB_WORLD_PAY_SHOPPING_LOAN"
    GOOGLEPAY = "GOOGLEPAY"
    GARANTI_PAY = "GARANTI_PAY"
