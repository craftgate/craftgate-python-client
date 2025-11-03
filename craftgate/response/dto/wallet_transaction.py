from decimal import Decimal
from typing import Optional

from craftgate.model.wallet_transaction_type import WalletTransactionType


class WalletTransaction(object):
    def __init__(
            self,
            id: Optional[int] = None,
            wallet_transaction_type: Optional[WalletTransactionType] = None,
            amount: Optional[Decimal] = None,
            wallet_id: Optional[int] = None
    ) -> None:
        self.id = id
        self.wallet_transaction_type = wallet_transaction_type
        self.amount = amount
        self.wallet_id = wallet_id
