from datetime import datetime
from decimal import Decimal
from typing import Optional, Set

from craftgate.model.currency import Currency
from craftgate.model.status import Status


class ProductResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            description: Optional[str] = None,
            order_id: Optional[str] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            status: Optional[Status] = None,
            price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            stock: Optional[int] = None,
            sold_count: Optional[int] = None,
            token: Optional[str] = None,
            enabled_installments: Optional[Set[int]] = None,
            url: Optional[str] = None,
            multi_payment: Optional[bool] = None,
            channel: Optional[str] = None,
            expires_at: Optional[datetime] = None
    ) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.order_id = order_id
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.status = status
        self.price = price
        self.currency = currency
        self.stock = stock
        self.sold_count = sold_count
        self.token = token
        self.enabled_installments = enabled_installments
        self.url = url
        self.multi_payment = multi_payment
        self.channel = channel
        self.expires_at = expires_at
