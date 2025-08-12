from typing import Optional

from craftgate.model.currency import Currency
from craftgate.request.dto.card import Card


class CreateDepositPaymentRequest(object):
    def __init__(self,
                 buyer_member_id=None,  # type: Optional[int]
                 price=None,  # type: Optional[float]
                 currency=None,  # type: Optional[Currency]
                 conversation_id=None,  # type: Optional[str]
                 callback_url=None,  # type: Optional[str]
                 pos_alias=None,  # type: Optional[str]
                 client_ip=None,  # type: Optional[str]
                 card=None  # type: Optional[Card]
                 ):
        self.buyer_member_id = buyer_member_id
        self.price = price
        self.currency = currency
        self.conversation_id = conversation_id
        self.callback_url = callback_url
        self.pos_alias = pos_alias
        self.client_ip = client_ip
        self.card = card
