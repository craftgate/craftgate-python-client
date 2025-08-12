from typing import Optional
from craftgate.model.currency import Currency
from craftgate.model.account_owner import AccountOwner


class SearchPayoutAccountRequest(object):
    def __init__(
        self,
        currency=None,                # type: Optional[Currency]
        account_owner=None,           # type: Optional[AccountOwner]
        sub_merchant_member_id=None,  # type: Optional[int]
        page=0,                       # type: Optional[int]
        size=10                       # type: Optional[int]
    ):
        self.currency = currency
        self.account_owner = account_owner
        self.sub_merchant_member_id = sub_merchant_member_id
        self.page = page
        self.size = size
