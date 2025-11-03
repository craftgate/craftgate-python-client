from decimal import Decimal
from typing import Any, Dict, List, Optional

from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.model.payment_method import PaymentMethod
from craftgate.model.payment_phase import PaymentPhase
from craftgate.request.dto.custom_installment import CustomInstallment
from craftgate.request.dto.fraud_check_parameters import FraudCheckParameters
from craftgate.request.dto.payment_item import PaymentItem


class InitCheckoutPaymentRequest(object):
    def __init__(
            self,
            price: Optional[Decimal] = None,
            paid_price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            payment_group: Optional[PaymentGroup] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            order_id: Optional[str] = None,
            callback_url: Optional[str] = None,
            client_ip: Optional[str] = None,
            payment_phase: PaymentPhase = PaymentPhase.AUTH,
            payment_channel: Optional[str] = None,
            enabled_payment_methods: Optional[List[PaymentMethod]] = None,
            masterpass_gsm_number: Optional[str] = None,
            masterpass_user_id: Optional[str] = None,
            card_user_key: Optional[str] = None,
            buyer_member_id: Optional[int] = None,
            enabled_installments: Optional[List[int]] = None,
            always_store_card_after_payment: bool = False,
            allow_only_stored_cards: bool = False,
            allow_only_credit_card: bool = False,
            allow_installment_only_commercial_cards: bool = False,
            force_three_ds: bool = False,
            force_auth_for_non_credit_cards: bool = False,
            deposit_payment: bool = False,
            ttl: Optional[int] = None,
            custom_installments: Optional[List[CustomInstallment]] = None,
            items: Optional[List[PaymentItem]] = None,
            fraud_params: Optional[FraudCheckParameters] = None,
            additional_params: Optional[Dict[str, Any]] = None,
            card_brand_installments: Optional[Dict[str, List[CustomInstallment]]] = None
    ) -> None:
        self.price = price
        self.paid_price = paid_price
        self.currency = currency
        self.payment_group = payment_group
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.order_id = order_id
        self.callback_url = callback_url
        self.client_ip = client_ip
        self.payment_phase = payment_phase
        self.payment_channel = payment_channel
        self.enabled_payment_methods = enabled_payment_methods
        self.masterpass_gsm_number = masterpass_gsm_number
        self.masterpass_user_id = masterpass_user_id
        self.card_user_key = card_user_key
        self.buyer_member_id = buyer_member_id
        self.enabled_installments = enabled_installments
        self.always_store_card_after_payment = always_store_card_after_payment
        self.allow_only_stored_cards = allow_only_stored_cards
        self.allow_only_credit_card = allow_only_credit_card
        self.allow_installment_only_commercial_cards = allow_installment_only_commercial_cards
        self.force_three_ds = force_three_ds
        self.force_auth_for_non_credit_cards = force_auth_for_non_credit_cards
        self.deposit_payment = deposit_payment
        self.ttl = ttl
        self.custom_installments = custom_installments
        self.items = items
        self.fraud_params = fraud_params
        self.additional_params = additional_params
        self.card_brand_installments = card_brand_installments
