from decimal import Decimal
from typing import Optional

from craftgate.model.card_verification_auth_type import CardVerificationAuthType
from craftgate.model.currency import Currency
from craftgate.request.dto.verify_card import VerifyCard


class VerifyCardRequest(object):
    def __init__(
            self,
            card: Optional[VerifyCard] = None,
            payment_authentication_type: Optional[CardVerificationAuthType] = None,
            verification_price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            client_ip: Optional[str] = None,
            conversation_id: Optional[str] = None,
            callback_url: Optional[str] = None
    ) -> None:
        self.card = card
        self.payment_authentication_type = payment_authentication_type
        self.verification_price = verification_price
        self.currency = currency
        self.client_ip = client_ip
        self.conversation_id = conversation_id
        self.callback_url = callback_url
