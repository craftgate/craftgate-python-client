from decimal import Decimal
from typing import Optional


class CreateFundTransferDepositPaymentRequest(object):
    def __init__(
            self,
            price: Optional[Decimal] = None,
            buyer_member_id: Optional[int] = None,
            conversation_id: Optional[str] = None,
            client_ip: Optional[str] = None
    ) -> None:
        self.price = price
        self.buyer_member_id = buyer_member_id
        self.conversation_id = conversation_id
        self.client_ip = client_ip
