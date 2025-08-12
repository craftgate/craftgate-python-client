from typing import List


class ApprovePaymentTransactionsRequest(object):
    def __init__(self,
                 payment_transaction_ids,  # type: List[int]
                 is_transactional=False  # type: bool
                 ):
        self.payment_transaction_ids = payment_transaction_ids  # type: List[int]
        self.is_transactional = is_transactional  # type: bool
