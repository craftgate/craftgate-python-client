from typing import List

from craftgate.request.common.base_request import BaseRequest


class DisapprovePaymentTransactionsRequest(BaseRequest):
    def __init__(
            self,
            payment_transaction_ids: List[int],
            is_transactional: bool = False
    ) -> None:
        self.payment_transaction_ids = payment_transaction_ids
        self.is_transactional = is_transactional
