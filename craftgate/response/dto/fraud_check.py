from typing import Optional

from craftgate.model.status import Status
from craftgate.model.fraud_action import FraudAction
from craftgate.model.fraud_check_status import FraudCheckStatus
from craftgate.model.payment_status import PaymentStatus
from craftgate.request.dto.fraud_payment_data import FraudPaymentData


class FraudCheck:
    def __init__(
        self,
        id: Optional[int] = None,
        status: Optional[Status] = None,
        action: Optional[FraudAction] = None,
        check_status: Optional[FraudCheckStatus] = None,
        payment_data: Optional[FraudPaymentData] = None,
        rule_id: Optional[int] = None,
        rule_name: Optional[str] = None,
        rule_conditions: Optional[str] = None,
        payment_id: Optional[int] = None,
        payment_status: Optional[PaymentStatus] = None
    ) -> None:
        self.id = id
        self.status = status
        self.action = action
        self.check_status = check_status
        self.payment_data = payment_data
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_conditions = rule_conditions
        self.payment_id = payment_id
        self.payment_status = payment_status
