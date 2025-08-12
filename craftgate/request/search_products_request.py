from typing import Optional
from craftgate.model.currency import Currency


class SearchProductsRequest(object):
    def __init__(
        self,
        name=None,       # type: Optional[str]
        min_price=None,  # type: Optional[float]
        max_price=None,  # type: Optional[float]
        currency=None,   # type: Optional[Currency]
        channel=None,    # type: Optional[str]
        page=0,          # type: int
        size=25          # type: int
    ):
        self.name = name
        self.min_price = min_price
        self.max_price = max_price
        self.currency = currency
        self.channel = channel
        self.page = page
        self.size = size