from decimal import Decimal
from datetime import datetime
from typing import Optional

from craftgate.model.transaction_status import TransactionStatus
from craftgate.response.dto.payout import Payout


class PaymentTransaction:
    def __init__(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        external_id: Optional[str] = None,
        price: Optional[Decimal] = None,
        paid_price: Optional[Decimal] = None,
        wallet_price: Optional[Decimal] = None,
        merchant_commission_rate: Optional[Decimal] = None,
        merchant_commission_rate_amount: Optional[Decimal] = None,
        merchant_payout_amount: Optional[Decimal] = None,
        sub_merchant_member_id: Optional[int] = None,
        sub_merchant_member_price: Optional[Decimal] = None,
        sub_merchant_member_payout_rate: Optional[Decimal] = None,
        sub_merchant_member_payout_amount: Optional[Decimal] = None,
        transaction_status: Optional[TransactionStatus] = None,
        blockage_resolved_date: Optional[datetime] = None,
        payout: Optional[Payout] = None
    ) -> None:
        self.id = id
        self.name = name
        self.external_id = external_id
        self.price = price
        self.paid_price = paid_price
        self.wallet_price = wallet_price
        self.merchant_commission_rate = merchant_commission_rate
        self.merchant_commission_rate_amount = merchant_commission_rate_amount
        self.merchant_payout_amount = merchant_payout_amount
        self.sub_merchant_member_id = sub_merchant_member_id
        self.sub_merchant_member_price = sub_merchant_member_price
        self.sub_merchant_member_payout_rate = sub_merchant_member_payout_rate
        self.sub_merchant_member_payout_amount = sub_merchant_member_payout_amount
        self.transaction_status = transaction_status
        self.blockage_resolved_date = blockage_resolved_date
        self.payout = payout
