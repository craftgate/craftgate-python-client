from typing import Optional

from craftgate.model.payout_account_type import PayoutAccountType
from craftgate.model.currency import Currency
from craftgate.model.account_owner import AccountOwner


class CreatePayoutAccountRequest(object):
    def __init__(
            self,
            type: Optional[PayoutAccountType] = None,
            external_account_id: Optional[str] = None,
            currency: Optional[Currency] = None,
            account_owner: Optional[AccountOwner] = None,
            sub_merchant_member_id: Optional[int] = None
    ) -> None:
        self.type = type
        self.external_account_id = external_account_id
        self.currency = currency
        self.account_owner = account_owner
        self.sub_merchant_member_id = sub_merchant_member_id
