from datetime import datetime
from decimal import Decimal
from typing import Optional


class FraudPaymentData:
    def __init__(
            self,
            payment_date: Optional[datetime] = None,
            conversation_id: Optional[str] = None,
            paid_price: Optional[Decimal] = None,
            currency: Optional[str] = None,
            buyer_id: Optional[int] = None,
            client_ip: Optional[str] = None
    ) -> None:
        self.payment_date = payment_date
        self.conversation_id = conversation_id
        self.paid_price = paid_price
        self.currency = currency
        self.buyer_id = buyer_id
        self.client_ip = client_ip
