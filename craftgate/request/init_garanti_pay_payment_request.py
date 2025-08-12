from typing import Optional, List
from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.request.dto.payment_item import PaymentItem
from craftgate.request.dto.garanti_pay_installment import GarantiPayInstallment

class InitGarantiPayPaymentRequest(object):
    def __init__(
        self,
        price=None,                  # type: Optional[float]
        paid_price=None,              # type: Optional[float]
        currency=None,                # type: Optional[Currency]
        pos_alias=None,               # type: Optional[str]
        payment_group=None,           # type: Optional[PaymentGroup]
        conversation_id=None,         # type: Optional[str]
        external_id=None,              # type: Optional[str]
        callback_url=None,             # type: Optional[str]
        client_ip=None,                # type: Optional[str]
        payment_channel=None,          # type: Optional[str]
        buyer_member_id=None,          # type: Optional[int]
        bank_order_id=None,            # type: Optional[str]
        items=None,                    # type: Optional[List[PaymentItem]]
        installments=None,             # type: Optional[List[GarantiPayInstallment]]
        enabled_installments=None      # type: Optional[List[int]]
    ):
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
        self.items = items or []
        self.installments = installments or []
        self.enabled_installments = enabled_installments or []