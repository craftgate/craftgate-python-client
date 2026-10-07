from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class DeleteMerchantPosRequest(BaseRequest):
    def __init__(
            self,
            merchant_pos_id: Optional[int] = None
    ) -> None:
        self.merchant_pos_id = merchant_pos_id
