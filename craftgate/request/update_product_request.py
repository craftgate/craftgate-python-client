from datetime import datetime
from decimal import Decimal
from typing import Optional, Set

from craftgate.model.currency import Currency
from craftgate.model.status import Status


class UpdateProductRequest(object):
    def __init__(
            self,
            name: Optional[str] = None,
            channel: Optional[str] = None,
            order_id: Optional[str] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            status: Optional[Status] = None,
            stock: Optional[int] = None,
            price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            description: Optional[str] = None,
            expires_at: Optional[datetime] = None,
            multi_payment: bool = False,
            enabled_installments: Optional[Set[int]] = None
    ) -> None:
        self.name = name
        self.channel = channel
        self.order_id = order_id
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.status = status
        self.stock = stock
        self.price = price
        self.currency = currency
        self.description = description
        self.expires_at = expires_at
        self.multi_payment = multi_payment
        self.enabled_installments = enabled_installments
