from typing import Optional

from craftgate.model.pos_status import PosStatus
from craftgate.request.common.base_request import BaseRequest


class UpdateMerchantPosStatusRequest(BaseRequest):
    def __init__(
            self,
            merchant_pos_id: Optional[int] = None,
            pos_status: Optional[PosStatus] = None
    ) -> None:
        self.merchant_pos_id = merchant_pos_id
        self.pos_status = pos_status
