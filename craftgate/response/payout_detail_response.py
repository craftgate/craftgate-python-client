from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from craftgate.model.bounce_status import BounceStatus
from craftgate.response.dto.payout_detail_transaction import PayoutDetailTransaction


class PayoutDetailResponse(object):
    def __init__(
            self,
            row_description: Optional[str] = None,
            payout_date: Optional[datetime] = None,
            name: Optional[str] = None,
            iban: Optional[str] = None,
            payout_amount: Optional[Decimal] = None,
            currency: Optional[str] = None,
            merchant_id: Optional[int] = None,
            merchant_type: Optional[str] = None,
            settlement_earnings_destination: Optional[str] = None,
            settlement_source: Optional[str] = None,
            bounce_status: Optional[BounceStatus] = None,
            payout_transactions: Optional[List[PayoutDetailTransaction]] = None
    ) -> None:
        self.row_description = row_description
        self.payout_date = payout_date
        self.name = name
        self.iban = iban
        self.payout_amount = payout_amount
        self.currency = currency
        self.merchant_id = merchant_id
        self.merchant_type = merchant_type
        self.settlement_earnings_destination = settlement_earnings_destination
        self.settlement_source = settlement_source
        self.bounce_status = bounce_status
        self.payout_transactions = payout_transactions
