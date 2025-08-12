from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.merchant_type import MerchantType
from craftgate.model.settlement_earnings_destination import SettlementEarningsDestination
from craftgate.model.settlement_source import SettlementSource


class PayoutCompletedTransaction(object):
    def __init__(
            self,
            payout_id: Optional[int] = None,
            transaction_id: Optional[int] = None,
            transaction_type: Optional[str] = None,
            payout_amount: Optional[Decimal] = None,
            payout_date: Optional[datetime] = None,
            currency: Optional[str] = None,
            merchant_id: Optional[int] = None,
            merchant_type: Optional[MerchantType] = None,
            settlement_earnings_destination: Optional[SettlementEarningsDestination] = None,
            settlement_source: Optional[SettlementSource] = None
    ) -> None:
        self.payout_id = payout_id
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.payout_amount = payout_amount
        self.payout_date = payout_date
        self.currency = currency
        self.merchant_id = merchant_id
        self.merchant_type = merchant_type
        self.settlement_earnings_destination = settlement_earnings_destination
        self.settlement_source = settlement_source
