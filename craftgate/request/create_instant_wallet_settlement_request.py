from typing import Optional, List


class CreateInstantWalletSettlementRequest(object):
    def __init__(self, excluded_sub_merchant_member_ids=None):
        # type: (Optional[List[int]]) -> None
        self.excluded_sub_merchant_member_ids = excluded_sub_merchant_member_ids
