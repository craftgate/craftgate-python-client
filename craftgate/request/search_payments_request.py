from datetime import datetime
from typing import Optional

from craftgate.model.currency import Currency
from craftgate.model.payment_provider import PaymentProvider
from craftgate.model.payment_source import PaymentSource
from craftgate.model.payment_status import PaymentStatus
from craftgate.model.payment_type import PaymentType


class SearchPaymentsRequest(object):
    def __init__(
            self,
            page=None,  # type: Optional[int]
            size=None,  # type: Optional[int]
            payment_id=None,  # type: Optional[int]
            payment_transaction_id=None,  # type: Optional[int]
            buyer_member_id=None,  # type: Optional[int]
            sub_merchant_member_id=None,  # type: Optional[int]
            conversation_id=None,  # type: Optional[str]
            external_id=None,  # type: Optional[str]
            order_id=None,  # type: Optional[str]
            payment_type=None,  # type: Optional[PaymentType]
            payment_provider=None,  # type: Optional[PaymentProvider]
            payment_status=None,  # type: Optional[PaymentStatus]
            payment_source=None,  # type: Optional[PaymentSource]
            payment_channel=None,  # type: Optional[str]
            bin_number=None,  # type: Optional[str]
            last_four_digits=None,  # type: Optional[str]
            currency=None,  # type: Optional[Currency]
            min_paid_price=None,  # type: Optional[decimal]
            max_paid_price=None,  # type: Optional[decimal]
            installment=None,  # type: Optional[int]
            is_three_ds=None,  # type: Optional[bool]
            min_created_date=None,  # type: Optional[datetime]
            max_created_date=None  # type: Optional[datetime]
    ):
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
