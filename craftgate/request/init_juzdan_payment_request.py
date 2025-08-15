import decimal
from typing import Optional, List

from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.model.payment_phase import PaymentPhase
from craftgate.request.dto.payment_item import PaymentItem


class InitJuzdanPaymentRequest(object):
    class ClientType:
        M = "M"
        W = "W"

    def __init__(
            self,
            price=None,  # type: Optional[Decimal]
            paid_price=None,  # type: Optional[Decimal]
            currency=None,  # type: Optional[Currency]
            payment_group=None,  # type: Optional[PaymentGroup]
            conversation_id=None,  # type: Optional[str]
            external_id=None,  # type: Optional[str]
            callback_url=None,  # type: Optional[str]
            payment_phase=PaymentPhase.AUTH,  # type: PaymentPhase
            payment_channel=None,  # type: Optional[str]
            buyer_member_id=None,  # type: Optional[int]
            bank_order_id=None,  # type: Optional[str]
            items=None,  # type: Optional[List[PaymentItem]]
            client_type=None,  # type: Optional[str]
            loan_campaign_id=None  # type: Optional[int]
    ):
        self.price = price
        self.paid_price = paid_price
        self.currency = currency
        self.payment_group = payment_group
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.callback_url = callback_url
        self.payment_phase = payment_phase
        self.payment_channel = payment_channel
        self.buyer_member_id = buyer_member_id
        self.bank_order_id = bank_order_id
        self.items = items
        self.client_type = client_type
        self.loan_campaign_id = loan_campaign_id
