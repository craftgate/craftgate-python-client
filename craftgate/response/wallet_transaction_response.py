from typing import Optional
from decimal import Decimal
from datetime import datetime

from craftgate.model.wallet_transaction_type import WalletTransactionType


class WalletTransactionResponse(object):
    def __init__(
        self,
        id=None,  # type: Optional[int]
        created_date=None,  # type: Optional[datetime]
        wallet_transaction_type=None,  # type: Optional[WalletTransactionType]
        amount=None,  # type: Optional[Decimal]
        transaction_id=None,  # type: Optional[int]
        wallet_id=None  # type: Optional[int]
    ):
        self.id = id
        self.created_date = created_date
        self.wallet_transaction_type = wallet_transaction_type
        self.amount = amount
        self.transaction_id = transaction_id
        self.wallet_id = wallet_id
