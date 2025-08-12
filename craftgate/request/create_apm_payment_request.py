from typing import Optional, List

from craftgate.model.apm_type import ApmType
from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.request.dto.payment_item import PaymentItem


class CreateApmPaymentRequest(object):
    def __init__(self,
                 apm_type=None,  # type: Optional[ApmType]
                 price=None,  # type: Optional[float]
                 paid_price=None,  # type: Optional[float]
                 currency=None,  # type: Optional[Currency]
                 payment_group=None,  # type: Optional[PaymentGroup]
                 payment_channel=None,  # type: Optional[str]
                 conversation_id=None,  # type: Optional[str]
                 external_id=None,  # type: Optional[str]
                 buyer_member_id=None,  # type: Optional[int]
                 apm_order_id=None,  # type: Optional[str]
                 client_ip=None,  # type: Optional[str]
                 items=None  # type: Optional[List[PaymentItem]]
                 ):
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
