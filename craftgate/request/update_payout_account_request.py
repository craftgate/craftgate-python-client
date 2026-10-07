from typing import Optional

from craftgate.model.payout_account_type import PayoutAccountType
from craftgate.request.common.base_request import BaseRequest


class UpdatePayoutAccountRequest(BaseRequest):
    def __init__(
            self,
            type: Optional[PayoutAccountType] = None,
            external_account_id: Optional[str] = None
    ) -> None:
        self.type = type
        self.external_account_id = external_account_id
