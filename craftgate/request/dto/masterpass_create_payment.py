import decimal
from typing import Optional, List, Dict, Any

from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.model.payment_phase import PaymentPhase
from craftgate.request.dto.payment_item import PaymentItem


class MasterpassCreatePayment(object):
    def __init__(
            self,
            price=None,  # type: Optional[decimal]
            paid_price=None,  # type: Optional[decimal]
            pos_alias=None,  # type: Optional[str]
            installment=None,  # type: Optional[int]
            currency=None,  # type: Optional[Currency]
            payment_group=None,  # type: Optional[PaymentGroup]
            conversation_id=None,  # type: Optional[str]
            external_id=None,  # type: Optional[str]
            client_ip=None,  # type: Optional[str]
            payment_phase=PaymentPhase.AUTH,  # type: PaymentPhase
            payment_channel=None,  # type: Optional[str]
            buyer_member_id=None,  # type: Optional[int]
            bank_order_id=None,  # type: Optional[str]
            items=None,  # type: Optional[List[PaymentItem]]
            additional_params=None  # type: Optional[Dict[str, Any]]
    ):
        self.price = price
        self.paid_price = paid_price
        self.pos_alias = pos_alias
        self.installment = installment
        self.currency = currency
        self.payment_group = payment_group
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.client_ip = client_ip
        self.payment_phase = payment_phase
        self.payment_channel = payment_channel
        self.buyer_member_id = buyer_member_id
        self.bank_order_id = bank_order_id
        self.items = items
        self.additional_params = additional_params
