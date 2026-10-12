from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.request.common.base_request import BaseRequest


class CreateWithdrawRequest(BaseRequest):
    def __init__(
            self,
            price: Optional[Decimal] = None,
            member_id: Optional[int] = None,
            description: Optional[str] = None,
            currency: Optional[Currency] = None
    ) -> None:
        self.price = price
        self.member_id = member_id
        self.description = description
        self.currency = currency
