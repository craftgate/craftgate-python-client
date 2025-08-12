from decimal import Decimal
from typing import Optional, List

from craftgate.model.apm_type import ApmType
from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.request.dto.payment_item import PaymentItem


class CreateApmPaymentRequest(object):
    def __init__(
            self,
            apm_type: Optional[ApmType] = None,
            price: Optional[Decimal] = None,
            paid_price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            payment_group: Optional[PaymentGroup] = None,
            payment_channel: Optional[str] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            buyer_member_id: Optional[int] = None,
            apm_order_id: Optional[str] = None,
            client_ip: Optional[str] = None,
            items: Optional[List[PaymentItem]] = None
    ) -> None:
        self.apm_type = apm_type
        self.price = price
        self.paid_price = paid_price
        self.currency = currency
        self.payment_group = payment_group
        self.payment_channel = payment_channel
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.buyer_member_id = buyer_member_id
        self.apm_order_id = apm_order_id
        self.client_ip = client_ip
        self.items = items
