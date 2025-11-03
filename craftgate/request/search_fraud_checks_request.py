from datetime import datetime
from typing import Optional

from craftgate.model.fraud_action import FraudAction
from craftgate.model.fraud_check_status import FraudCheckStatus
from craftgate.model.payment_status import PaymentStatus


class SearchFraudChecksRequest(object):
    def __init__(
            self,
            page: Optional[int] = None,
            size: Optional[int] = None,
            action: Optional[FraudAction] = None,
            check_status: Optional[FraudCheckStatus] = None,
            min_created_date: Optional[datetime] = None,
            max_created_date: Optional[datetime] = None,
            rule_id: Optional[int] = None,
            payment_id: Optional[int] = None,
            payment_status: Optional[PaymentStatus] = None
    ) -> None:
        self.page = page
        self.size = size
        self.action = action
        self.check_status = check_status
        self.min_created_date = min_created_date
        self.max_created_date = max_created_date
        self.rule_id = rule_id
        self.payment_id = payment_id
        self.payment_status = payment_status
