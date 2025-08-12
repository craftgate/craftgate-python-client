from typing import Optional
from craftgate.model.payout_account_type import PayoutAccountType


class UpdatePayoutAccountRequest(object):
    def __init__(
        self,
        type=None,                    # type: Optional[PayoutAccountType]
        external_account_id=None      # type: Optional[str]
    ):
        self.type = type
        self.external_account_id = external_account_id
