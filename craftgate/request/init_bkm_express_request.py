import decimal
from decimal import Decimal
from typing import List, Optional

from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.model.payment_phase import PaymentPhase
from craftgate.request.dto.payment_item import PaymentItem


class InitBkmExpressRequest:
    def __init__(
        self,
        price: Optional[decimal] = None,
        paid_price: Optional[decimal] = None,
        payment_group: Optional[PaymentGroup] = None,
        conversation_id: Optional[str] = None,
        payment_phase: Optional[PaymentPhase] = None,
        items: Optional[List[PaymentItem]] = None,
        enabled_installments: Optional[List[int]] = None,
        buyer_member_id: Optional[int] = None,
        currency: Optional[Currency] = None,
        bank_order_id: Optional[str] = None
    ) -> None:
        self.price = price
        self.paid_price = paid_price
        self.payment_group = payment_group
        self.conversation_id = conversation_id
        self.payment_phase = payment_phase
        self.items = items
        self.enabled_installments = enabled_installments
        self.buyer_member_id = buyer_member_id
        self.currency = currency
        self.bank_order_id = bank_order_id
