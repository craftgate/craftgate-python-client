from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.model.payment_provider import PaymentProvider
from craftgate.model.payment_source import PaymentSource
from craftgate.model.payment_status import PaymentStatus
from craftgate.model.payment_type import PaymentType


class SearchPaymentsRequest(object):
    def __init__(
            self,
            page: Optional[int] = None,
            size: Optional[int] = None,
            payment_id: Optional[int] = None,
            payment_transaction_id: Optional[int] = None,
            buyer_member_id: Optional[int] = None,
            sub_merchant_member_id: Optional[int] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            order_id: Optional[str] = None,
            payment_type: Optional[PaymentType] = None,
            payment_provider: Optional[PaymentProvider] = None,
            payment_status: Optional[PaymentStatus] = None,
            payment_source: Optional[PaymentSource] = None,
            payment_channel: Optional[str] = None,
            bin_number: Optional[str] = None,
            last_four_digits: Optional[str] = None,
            currency: Optional[Currency] = None,
            min_paid_price: Optional[Decimal] = None,
            max_paid_price: Optional[Decimal] = None,
            installment: Optional[int] = None,
            is_three_ds: Optional[bool] = None,
            min_created_date: Optional[datetime] = None,
            max_created_date: Optional[datetime] = None
    ) -> None:
        self.page = page
        self.size = size
        self.payment_id = payment_id
        self.payment_transaction_id = payment_transaction_id
        self.buyer_member_id = buyer_member_id
        self.sub_merchant_member_id = sub_merchant_member_id
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.order_id = order_id
        self.payment_type = payment_type
        self.payment_provider = payment_provider
        self.payment_status = payment_status
        self.payment_source = payment_source
        self.payment_channel = payment_channel
        self.bin_number = bin_number
        self.last_four_digits = last_four_digits
        self.currency = currency
        self.min_paid_price = min_paid_price
        self.max_paid_price = max_paid_price
        self.installment = installment
        self.is_three_ds = is_three_ds
        self.min_created_date = min_created_date
        self.max_created_date = max_created_date
