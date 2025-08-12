from decimal import Decimal
from typing import Optional, List, Dict, Any

from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.model.payment_phase import PaymentPhase
from craftgate.request.dto.card import Card
from craftgate.request.dto.fraud_check_parameters import FraudCheckParameters
from craftgate.request.dto.payment_item import PaymentItem


class CreatePaymentRequest(object):
    def __init__(
            self,
            price: Optional[Decimal] = None,
            paid_price: Optional[Decimal] = None,
            wallet_price: Decimal = Decimal("0"),
            pos_alias: Optional[str] = None,
            installment: Optional[int] = None,
            currency: Optional[Currency] = None,
            payment_group: Optional[PaymentGroup] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            client_ip: Optional[str] = None,
            payment_phase: PaymentPhase = PaymentPhase.AUTH,
            payment_channel: Optional[str] = None,
            buyer_member_id: Optional[int] = None,
            bank_order_id: Optional[str] = None,
            card: Optional[Card] = None,
            fraud_params: Optional[FraudCheckParameters] = None,
            items: Optional[List[PaymentItem]] = None,
            additional_params: Optional[Dict[str, Any]] = None,
            retry: bool = True
    ) -> None:
        self.price = price
        self.paid_price = paid_price
        self.wallet_price = wallet_price
        self.pos_alias = pos_alias
        self.installment = installment
        self.currency = currency
        self.payment_group = payment_group
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.client_ip = client_ip
        self.payment_phase = payment_phase
        self.payment_channel = payment_channel
        self.buyer_member_id = buyer_member_id
        self.bank_order_id = bank_order_id
        self.card = card
        self.fraud_params = fraud_params
        self.items = items
        self.additional_params = additional_params
        self.retry = retry
