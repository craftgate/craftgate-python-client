from typing import Optional, List

class DisapprovePaymentTransactionsRequest(object):
    def __init__(self,
                 payment_transaction_ids=None,  # type: Optional[List[int]]
                 is_transactional=False         # type: bool
                 ):
        self.payment_transaction_ids = payment_transaction_ids
        self.is_transactional = is_transactional