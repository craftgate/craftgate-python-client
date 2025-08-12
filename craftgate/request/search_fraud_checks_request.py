from datetime import datetime
from typing import Optional

from craftgate.model.fraud_action import FraudAction
from craftgate.model.fraud_check_status import FraudCheckStatus
from craftgate.model.payment_status import PaymentStatus


class SearchFraudChecksRequest(object):
    def __init__(
        self,
        page=None,                          # type: Optional[int]
        size=None,                          # type: Optional[int]
        action=None,                        # type: Optional[FraudAction]
        check_status=None,                  # type: Optional[FraudCheckStatus]
        min_created_date=None,              # type: Optional[datetime]
        max_created_date=None,              # type: Optional[datetime]
        rule_id=None,                       # type: Optional[int]
        payment_id=None,                    # type: Optional[int]
        payment_status=None                 # type: Optional[PaymentStatus]
    ):
        # type: (...) -> None
        self.page = page
        self.size = size
        self.action = action
        self.check_status = check_status
        self.min_created_date = min_created_date
        self.max_created_date = max_created_date
        self.rule_id = rule_id
        self.payment_id = payment_id
        self.payment_status = payment_status
