import decimal
from typing import Optional, Set

from craftgate.model.currency import Currency


class CreateProductRequest(object):
    def __init__(
            self,
            name=None,  # type: Optional[str]
            channel=None,  # type: Optional[str]
            order_id=None,  # type: Optional[str]
            conversation_id=None,  # type: Optional[str]
            external_id=None,  # type: Optional[str]
            stock=None,  # type: Optional[int]
            price=None,  # type: Optional[decimal]
            currency=None,  # type: Optional[Currency]
            description=None,  # type: Optional[str]
            multi_payment=None,  # type: Optional[bool]
            enabled_installments=None  # type: Optional[Set[int]]
    ):
        self.name = name
        self.channel = channel
        self.order_id = order_id
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.stock = stock
        self.price = price
        self.currency = currency
        self.description = description
        self.multi_payment = multi_payment
        self.enabled_installments = enabled_installments
