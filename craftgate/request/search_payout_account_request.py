from typing import Optional

from craftgate.model.account_owner import AccountOwner
from craftgate.model.currency import Currency


class SearchPayoutAccountRequest(object):
    def __init__(
            self,
            currency: Optional[Currency] = None,
            account_owner: Optional[AccountOwner] = None,
            sub_merchant_member_id: Optional[int] = None,
            page: int = 0,
            size: int = 10
    ) -> None:
        self.currency = currency
        self.account_owner = account_owner
        self.sub_merchant_member_id = sub_merchant_member_id
        self.page = page
        self.size = size
