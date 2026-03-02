from decimal import Decimal
from typing import Optional

from craftgate.model.card_verification_auth_type import CardVerificationAuthType
from craftgate.model.currency import Currency


class InitCheckoutCardVerifyRequest(object):
    def __init__(
            self,
            verification_price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            conversation_id: Optional[str] = None,
            callback_url: Optional[str] = None,
            card_user_key: Optional[str] = None,
            payment_authentication_type: Optional[CardVerificationAuthType] = None,
            ttl: Optional[int] = None
    ) -> None:
        self.verification_price = verification_price
        self.currency = currency
        self.conversation_id = conversation_id
        self.callback_url = callback_url
        self.card_user_key = card_user_key
        self.payment_authentication_type = payment_authentication_type
        self.ttl = ttl
