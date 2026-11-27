from typing import List

from craftgate.request.common.base_request import BaseRequest


class SearchPaymentTransactionPayoutsRequest(BaseRequest):
    def __init__(
            self,
            payment_transaction_ids: List[int]
    ) -> None:
        self.payment_transaction_ids = payment_transaction_ids
