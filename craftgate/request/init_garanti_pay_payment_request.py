from decimal import Decimal
from typing import List, Optional

from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.request.dto.garanti_pay_installment import GarantiPayInstallment
from craftgate.request.dto.payment_item import PaymentItem


class InitGarantiPayPaymentRequest(object):
    def __init__(
            self,
            price: Optional[Decimal] = None,
            paid_price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            pos_alias: Optional[str] = None,
            payment_group: Optional[PaymentGroup] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            callback_url: Optional[str] = None,
            client_ip: Optional[str] = None,
            payment_channel: Optional[str] = None,
            buyer_member_id: Optional[int] = None,
            bank_order_id: Optional[str] = None,
            items: Optional[List[PaymentItem]] = None,
            installments: Optional[List[GarantiPayInstallment]] = None,
            enabled_installments: Optional[List[int]] = None
    ) -> None:
        self.price = price
        self.paid_price = paid_price
        self.currency = currency
        self.pos_alias = pos_alias
        self.payment_group = payment_group
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.callback_url = callback_url
        self.client_ip = client_ip
        self.payment_channel = payment_channel
        self.buyer_member_id = buyer_member_id
        self.bank_order_id = bank_order_id
        self.items = items
        self.installments = installments
        self.enabled_installments = enabled_installments
