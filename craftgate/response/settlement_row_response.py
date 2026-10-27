from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from craftgate.model.bounce_status import BounceStatus
from craftgate.model.currency import Currency
from craftgate.model.merchant_type import MerchantType
from craftgate.model.settlement_earnings_destination import SettlementEarningsDestination
from craftgate.model.settlement_source import SettlementSource
from craftgate.response.dto.settlement_row_item import SettlementRowItem


class SettlementRowResponse(object):
    def __init__(
            self,
            row_description: Optional[str] = None,
            payout_date: Optional[datetime] = None,
            name: Optional[str] = None,
            iban: Optional[str] = None,
            payout_amount: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            merchant_type: Optional[MerchantType] = None,
            merchant_id: Optional[int] = None,
            settlement_earnings_destination: Optional[SettlementEarningsDestination] = None,
            settlement_source: Optional[SettlementSource] = None,
            bounce_status: Optional[BounceStatus] = None,
            items: Optional[List[SettlementRowItem]] = None
    ) -> None:
        self.row_description = row_description
        self.payout_date = payout_date
        self.name = name
        self.iban = iban
        self.payout_amount = payout_amount
        self.currency = currency
        self.merchant_type = merchant_type
        self.merchant_id = merchant_id
        self.settlement_earnings_destination = settlement_earnings_destination
        self.settlement_source = settlement_source
        self.bounce_status = bounce_status
        self.items = items
