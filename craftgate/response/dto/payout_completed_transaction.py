from typing import Optional
from datetime import datetime
from craftgate.model.merchant_type import MerchantType
from craftgate.model.settlement_earnings_destination import SettlementEarningsDestination
from craftgate.model.settlement_source import SettlementSource


class PayoutCompletedTransaction(object):
    def __init__(
        self,
        payout_id=None,                          # type: Optional[int]
        transaction_id=None,                     # type: Optional[int]
        transaction_type=None,                   # type: Optional[str]
        payout_amount=None,                      # type: Optional[float]
        payout_date=None,                        # type: Optional[datetime]
        currency=None,                           # type: Optional[str]
        merchant_id=None,                        # type: Optional[int]
        merchant_type=None,                      # type: Optional[MerchantType]
        settlement_earnings_destination=None,    # type: Optional[SettlementEarningsDestination]
        settlement_source=None                   # type: Optional[SettlementSource]
    ):
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
