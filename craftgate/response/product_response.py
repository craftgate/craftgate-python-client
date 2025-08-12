from typing import Optional, Set
from craftgate.model.currency import Currency
from craftgate.model.status import Status


class ProductResponse(object):
    def __init__(
        self,
        id=None,                     # type: Optional[int]
        name=None,                   # type: Optional[str]
        description=None,             # type: Optional[str]
        order_id=None,                # type: Optional[str]
        conversation_id=None,         # type: Optional[str]
        external_id=None,             # type: Optional[str]
        status=None,                  # type: Optional[Status]
        price=None,                   # type: Optional[float]
        currency=None,                # type: Optional[Currency]
        stock=None,                   # type: Optional[int]
        sold_count=None,              # type: Optional[int]
        token=None,                   # type: Optional[str]
        enabled_installments=None,    # type: Optional[Set[int]]
        url=None,                     # type: Optional[str]
        qr_code_url=None,             # type: Optional[str]
        channel=None                  # type: Optional[str]
    ):
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
        self.qr_code_url = qr_code_url
        self.channel = channel