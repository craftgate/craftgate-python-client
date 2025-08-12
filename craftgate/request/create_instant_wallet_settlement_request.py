from typing import List, Optional


class CreateInstantWalletSettlementRequest(object):
    def __init__(
            self,
            excluded_sub_merchant_member_ids: Optional[List[int]] = None
    ) -> None:
        self.excluded_sub_merchant_member_ids = excluded_sub_merchant_member_ids
