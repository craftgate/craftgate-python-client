from typing import Optional

from craftgate.model.payout_account_type import PayoutAccountType
from craftgate.model.account_owner import AccountOwner
from craftgate.model.currency import Currency


class PayoutAccountResponse(object):
    def __init__(
        self,
        id=None,                      # type: Optional[int]
        type=None,                    # type: Optional[PayoutAccountType]
        external_account_id=None,     # type: Optional[str]
        currency=None,                # type: Optional[Currency]
        account_owner=None,           # type: Optional[AccountOwner]
        sub_merchant_member_id=None   # type: Optional[int]
    ):
        self.id = id
        self.type = type
        self.external_account_id = external_account_id
        self.currency = currency
        self.account_owner = account_owner
        self.sub_merchant_member_id = sub_merchant_member_id
