from datetime import datetime
from decimal import Decimal
from typing import Optional, Set

from craftgate.model.wallet_transaction_type import WalletTransactionType


class SearchWalletTransactionsRequest(object):
    def __init__(
            self,
            page: int = 0,
            size: int = 10,
            wallet_transaction_types: Optional[Set[WalletTransactionType]] = None,
            min_created_date: Optional[datetime] = None,
            max_created_date: Optional[datetime] = None,
            min_amount: Optional[Decimal] = None,
            max_amount: Optional[Decimal] = None
    ) -> None:
        self.page = page
        self.size = size
        self.wallet_transaction_types = wallet_transaction_types
        self.min_created_date = min_created_date
        self.max_created_date = max_created_date
        self.min_amount = min_amount
        self.max_amount = max_amount
