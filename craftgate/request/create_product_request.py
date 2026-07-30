from datetime import datetime
from decimal import Decimal
from typing import Optional, Set

from craftgate.model.currency import Currency


class CreateProductRequest(object):
    def __init__(
            self,
            name: Optional[str] = None,
            channel: Optional[str] = None,
            order_id: Optional[str] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            stock: Optional[int] = None,
            price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            expires_at: Optional[datetime] = None,
            description: Optional[str] = None,
            multi_payment: bool = False,
            enabled_installments: Optional[Set[int]] = None,
            basket_identifier: Optional[str] = None
    ) -> None:
        self.name = name
        self.channel = channel
        self.order_id = order_id
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.stock = stock
        self.price = price
        self.currency = currency
        self.expires_at = expires_at
        self.description = description
        self.multi_payment = multi_payment
        self.enabled_installments = enabled_installments
        self.basket_identifier = basket_identifier
