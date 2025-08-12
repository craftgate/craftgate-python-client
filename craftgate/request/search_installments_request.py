from typing import Optional

from craftgate.model.currency import Currency


class SearchInstallmentsRequest(object):
    def __init__(
        self,
        bin_number=None,                                # type: Optional[str]
        price=None,                                     # type: Optional[float]
        currency=None,                                  # type: Optional[Currency]
        distinct_card_brands_with_lowest_commissions=False,  # type: bool
        loyalty_exists=False                            # type: bool
    ):
        self.bin_number = bin_number
        self.price = price
        self.currency = currency
        self.distinct_card_brands_with_lowest_commissions = distinct_card_brands_with_lowest_commissions
        self.loyalty_exists = loyalty_exists