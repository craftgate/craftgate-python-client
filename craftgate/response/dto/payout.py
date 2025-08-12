from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency


class Payout:
    def __init__(
        self,
        currency: Optional[Currency] = None,
        parity: Optional[Decimal] = None,
        paid_price: Optional[Decimal] = None,
        merchant_payout_amount: Optional[Decimal] = None,
        sub_merchant_member_payout_amount: Optional[Decimal] = None
    ) -> None:
        self.currency = currency
        self.parity = parity
        self.paid_price = paid_price
        self.merchant_payout_amount = merchant_payout_amount
        self.sub_merchant_member_payout_amount = sub_merchant_member_payout_amount
