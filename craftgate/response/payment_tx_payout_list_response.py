from craftgate.response.common.list_response import ListResponse
from craftgate.response.payment_tx_payout_response import PaymentTxPayoutResponse


class PaymentTxPayoutListResponse(ListResponse[PaymentTxPayoutResponse]):
    item_type = PaymentTxPayoutResponse
