from decimal import Decimal
from typing import Optional

from craftgate.response.dto.wallet_transaction import WalletTransaction


class FundTransferDepositPaymentResponse(object):
    def __init__(
            self,
            price: Optional[Decimal] = None,
            currency: Optional[str] = None,
            conversation_id: Optional[str] = None,
            buyer_member_id: Optional[int] = None,
            wallet_transaction: Optional[WalletTransaction] = None
    ) -> None:
        self.price = price
        self.currency = currency
        self.conversation_id = conversation_id
        self.buyer_member_id = buyer_member_id
        self.wallet_transaction = wallet_transaction
