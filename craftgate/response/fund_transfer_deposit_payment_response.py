from typing import Optional
from decimal import Decimal
from craftgate.response.dto.wallet_transaction import WalletTransaction

class FundTransferDepositPaymentResponse(object):
    def __init__(
        self,
        price=None,                # type: Optional[Decimal]
        currency=None,              # type: Optional[str]
        conversation_id=None,       # type: Optional[str]
        buyer_member_id=None,       # type: Optional[int]
        wallet_transaction=None     # type: Optional[WalletTransaction]
    ):
        self.price = price
        self.currency = currency
        self.conversation_id = conversation_id
        self.buyer_member_id = buyer_member_id
        self.wallet_transaction = wallet_transaction