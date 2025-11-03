from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency


class SearchProductsRequest(object):
    def __init__(
            self,
            name: Optional[str] = None,
            min_price: Optional[Decimal] = None,
            max_price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            channel: Optional[str] = None,
            min_expires_at: Optional[datetime] = None,
            max_expires_at: Optional[datetime] = None,
            page: int = 0,
            size: int = 25
    ) -> None:
        self.name = name
        self.min_price = min_price
        self.max_price = max_price
        self.currency = currency
        self.channel = channel
        self.min_expires_at = min_expires_at
        self.max_expires_at = max_expires_at
        self.page = page
        self.size = size
