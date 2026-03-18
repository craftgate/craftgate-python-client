from enum import Enum
from typing import Optional, List


class OrderingRule(str, Enum):
    ON_US = "ON_US"
    LOW_COMMISSION_RATE = "LOW_COMMISSION_RATE"
    IN_ORDER = "IN_ORDER"


class RoutingOptions(object):
    def __init__(
            self,
            ordering_rule: Optional[OrderingRule] = None,
            pos_aliases: Optional[List[str]] = None
    ) -> None:
        self.ordering_rule = ordering_rule
        self.pos_aliases = pos_aliases
