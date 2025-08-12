from craftgate.response.common.list_response import ListResponse
from craftgate.response.wallet_transaction_response import WalletTransactionResponse


class WalletTransactionListResponse(ListResponse[WalletTransactionResponse]):
    item_type = WalletTransactionResponse
