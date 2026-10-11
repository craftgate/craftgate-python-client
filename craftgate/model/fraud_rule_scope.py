from enum import Enum


class FraudRuleScope(str, Enum):
    MERCHANT = "MERCHANT"
    GLOBAL = "GLOBAL"
