from typing import Optional
from datetime import datetime

from craftgate.model.bounce_status import BounceStatus
from craftgate.response.dto.payout_detail_transaction import PayoutDetailTransaction


class PayoutDetailResponse(object):
    def __init__(
        self,
        row_description=None,                   # type: Optional[str]
        payout_date=None,                       # type: Optional[datetime]
        name=None,                               # type: Optional[str]
        iban=None,                               # type: Optional[str]
        payout_amount=None,                      # type: Optional[float]
        currency=None,                           # type: Optional[str]
        merchant_id=None,                        # type: Optional[int]
        merchant_type=None,                      # type: Optional[str]
        settlement_earnings_destination=None,    # type: Optional[str]
        settlement_source=None,                  # type: Optional[str]
        bounce_status=None,                      # type: Optional[BounceStatus]
        payout_transactions=None                 # type: Optional[list]
    ):
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
        self.payout_transactions = payout_transactions or []  # type: list[PayoutDetailTransaction]
