from typing import Optional

from craftgate.model.refund_destination_type import RefundDestinationType
from craftgate.request.common.base_request import BaseRequest


class RefundPaymentRequest(BaseRequest):
    def __init__(
            self,
            payment_id: Optional[int] = None,
            conversation_id: Optional[str] = None,
            refund_destination_type: RefundDestinationType = RefundDestinationType.PROVIDER,
            charge_from_me: bool = False
    ) -> None:
        self.payment_id = payment_id
        self.conversation_id = conversation_id
        self.refund_destination_type = refund_destination_type
        self.charge_from_me = charge_from_me
