from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class CancelWithdrawRequest(BaseRequest):
    def __init__(
            self,
            withdraw_id: Optional[int] = None
    ) -> None:
        self.withdraw_id = withdraw_id
