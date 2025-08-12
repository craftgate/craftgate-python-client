from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.request.dto.card import Card


class CreateDepositPaymentRequest(object):
    def __init__(
            self,
            buyer_member_id: Optional[int] = None,
            price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            conversation_id: Optional[str] = None,
            callback_url: Optional[str] = None,
            pos_alias: Optional[str] = None,
            client_ip: Optional[str] = None,
            card: Optional[Card] = None
    ) -> None:
        self.buyer_member_id = buyer_member_id
        self.price = price
        self.currency = currency
        self.conversation_id = conversation_id
        self.callback_url = callback_url
        self.pos_alias = pos_alias
        self.client_ip = client_ip
        self.card = card
