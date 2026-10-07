from typing import List, Optional

from craftgate.request.common.base_request import BaseRequest


class CreateInstantWalletSettlementRequest(BaseRequest):
    def __init__(
            self,
            excluded_sub_merchant_member_ids: Optional[List[int]] = None
    ) -> None:
        self.excluded_sub_merchant_member_ids = excluded_sub_merchant_member_ids
