from decimal import Decimal
from typing import Any, Dict, List, Optional
from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.model.payment_phase import PaymentPhase
from craftgate.model.pos_apm_payment_provider import PosApmPaymentProvider
from craftgate.request.dto.fraud_check_parameters import FraudCheckParameters
from craftgate.request.dto.payment_item import PaymentItem
from craftgate.request.dto.pos_apm_installment import PosApmInstallment


class InitPosApmPaymentRequest(object):
    def __init__(
            self,
            price: Optional[Decimal] = None,
            paid_price: Optional[Decimal] = None,
            pos_alias: Optional[str] = None,
            currency: Optional[Currency] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            callback_url: Optional[str] = None,
            payment_group: Optional[PaymentGroup] = None,
            payment_phase: PaymentPhase = PaymentPhase.AUTH,
            payment_channel: Optional[str] = None,
            buyer_member_id: Optional[int] = None,
            bank_order_id: Optional[str] = None,
            client_ip: Optional[str] = None,
            items: Optional[List[PaymentItem]] = None,
            additional_params: Optional[Dict[str, Any]] = None,
            installments: Optional[List[PosApmInstallment]] = None,
            payment_provider: Optional[PosApmPaymentProvider] = None,
            fraud_params: Optional[FraudCheckParameters] = None,
            checkout_form_token: Optional[str] = None
    ) -> None:
        self.price = price
        self.paid_price = paid_price
        self.pos_alias = pos_alias
        self.currency = currency
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.callback_url = callback_url
        self.payment_group = payment_group
        self.payment_phase = payment_phase
        self.payment_channel = payment_channel
        self.buyer_member_id = buyer_member_id
        self.bank_order_id = bank_order_id
        self.client_ip = client_ip
        self.items = items or []
        self.additional_params = additional_params or {}
        self.installments = installments or []
        self.payment_provider = payment_provider
        self.fraud_params = fraud_params
        self.checkout_form_token = checkout_form_token
