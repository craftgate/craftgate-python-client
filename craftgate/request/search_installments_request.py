from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency


class SearchInstallmentsRequest(object):
    def __init__(
            self,
            bin_number: Optional[str] = None,
            price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            distinct_card_brands_with_lowest_commissions: bool = False,
            loyalty_exists: bool = False
    ) -> None:
        self.bin_number = bin_number
        self.price = price
        self.currency = currency
        self.distinct_card_brands_with_lowest_commissions = distinct_card_brands_with_lowest_commissions
        self.loyalty_exists = loyalty_exists
