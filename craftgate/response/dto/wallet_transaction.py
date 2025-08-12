from typing import Optional
from decimal import Decimal
from craftgate.model.wallet_transaction_type import WalletTransactionType

class WalletTransaction(object):
    def __init__(
        self,
        id=None,                           # type: Optional[int]
        wallet_transaction_type=None,      # type: Optional[WalletTransactionType]
        amount=None,                        # type: Optional[Decimal]
        wallet_id=None                      # type: Optional[int]
    ):
        self.id = id
        self.wallet_transaction_type = wallet_transaction_type
        self.amount = amount
        self.wallet_id = wallet_id