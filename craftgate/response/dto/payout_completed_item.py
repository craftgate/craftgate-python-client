from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.model.merchant_type import MerchantType
from craftgate.model.settlement_earnings_destination import SettlementEarningsDestination
from craftgate.model.settlement_row_item_subject import SettlementRowItemSubject
from craftgate.model.settlement_source import SettlementSource


class PayoutCompletedItem(object):
    def __init__(
            self,
            settlement_row_id: Optional[int] = None,
            settlement_file_id: Optional[int] = None,
            subject: Optional[SettlementRowItemSubject] = None,
            subject_id: Optional[int] = None,
            payment_transaction_id: Optional[int] = None,
            merchant_type: Optional[MerchantType] = None,
            merchant_id: Optional[int] = None,
            payout_amount: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            payout_date: Optional[datetime] = None,
            settlement_earnings_destination: Optional[SettlementEarningsDestination] = None,
            settlement_source: Optional[SettlementSource] = None
    ) -> None:
        self.settlement_row_id = settlement_row_id
        self.settlement_file_id = settlement_file_id
        self.subject = subject
        self.subject_id = subject_id
        self.payment_transaction_id = payment_transaction_id
        self.merchant_type = merchant_type
        self.merchant_id = merchant_id
        self.payout_amount = payout_amount
        self.currency = currency
        self.payout_date = payout_date
        self.settlement_earnings_destination = settlement_earnings_destination
        self.settlement_source = settlement_source
