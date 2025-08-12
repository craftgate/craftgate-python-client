from craftgate.model.wallet_transaction_type import WalletTransactionType

class SearchWalletTransactionsRequest(object):
    def __init__(self):
        self.page = 0                             # type: int
        self.size = 10                            # type: int
        self.wallet_transaction_types = None      # type: list[WalletTransactionType]
        self.min_created_date = None              # type: datetime
        self.max_created_date = None              # type: datetime
        self.min_amount = None                    # type: Decimal
        self.max_amount = None                    # type: Decimal
