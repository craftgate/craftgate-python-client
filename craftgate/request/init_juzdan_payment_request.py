from decimal import Decimal
from typing import List, Optional

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
            price: Optional[Decimal] = None,
            paid_price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            payment_group: Optional[PaymentGroup] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            callback_url: Optional[str] = None,
            payment_phase: PaymentPhase = PaymentPhase.AUTH,
            payment_channel: Optional[str] = None,
            buyer_member_id: Optional[int] = None,
            bank_order_id: Optional[str] = None,
            items: Optional[List[PaymentItem]] = None,
            client_type: Optional[str] = None,
            loan_campaign_id: Optional[int] = None
    ) -> None:
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
