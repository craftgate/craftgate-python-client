from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.wallet_transaction_type import WalletTransactionType


class WalletTransactionResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            created_date: Optional[datetime] = None,
            wallet_transaction_type: Optional[WalletTransactionType] = None,
            amount: Optional[Decimal] = None,
            transaction_id: Optional[int] = None,
            wallet_id: Optional[int] = None
    ) -> None:
        self.id = id
        self.created_date = created_date
        self.wallet_transaction_type = wallet_transaction_type
        self.amount = amount
        self.transaction_id = transaction_id
        self.wallet_id = wallet_id
