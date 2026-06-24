from decimal import Decimal
from typing import Any, Dict, List, Optional

from craftgate.model.payment_source import PaymentSource
from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.model.payment_method import PaymentMethod
from craftgate.model.payment_phase import PaymentPhase
from craftgate.request.dto.payment_item import PaymentItem


class InitMultiPaymentRequest(object):
    def __init__(
            self,
            price: Optional[Decimal] = None,
            paid_price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            payment_group: Optional[PaymentGroup] = None,
            payment_source: Optional[PaymentSource] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            callback_url: Optional[str] = None,
            payment_phase: PaymentPhase = PaymentPhase.AUTH,
            payment_channel: Optional[str] = None,
            enabled_payment_methods: Optional[List[PaymentMethod]] = None,
            card_user_key: Optional[str] = None,
            buyer_member_id: Optional[int] = None,
            allow_only_credit_card: bool = False,
            force_auth_for_non_credit_cards: bool = False,
            allow_only_stored_cards: bool = False,
            allow_installment_only_commercial_cards: bool = False,
            always_store_card_after_payment: bool = False,
            disable_store_card: bool = False,
            force_three_ds: bool = False,
            masterpass_gsm_number: Optional[str] = None,
            masterpass_user_id: Optional[str] = None,
            apm_user_identity: Optional[str] = None,
            items: Optional[List[PaymentItem]] = None,
            ttl: Optional[int] = None,
            maximum_split_payment_count: Optional[int] = None,
            additional_params: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.price = price
        self.paid_price = paid_price
        self.currency = currency
        self.payment_group = payment_group
        self.payment_source = payment_source
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.callback_url = callback_url
        self.payment_phase = payment_phase
        self.payment_channel = payment_channel
        self.enabled_payment_methods = enabled_payment_methods
        self.masterpass_gsm_number = masterpass_gsm_number
        self.masterpass_user_id = masterpass_user_id
        self.apm_user_identity = apm_user_identity
        self.card_user_key = card_user_key
        self.buyer_member_id = buyer_member_id
        self.always_store_card_after_payment = always_store_card_after_payment
        self.disable_store_card = disable_store_card
        self.allow_only_stored_cards = allow_only_stored_cards
        self.allow_only_credit_card = allow_only_credit_card
        self.allow_installment_only_commercial_cards = allow_installment_only_commercial_cards
        self.force_three_ds = force_three_ds
        self.force_auth_for_non_credit_cards = force_auth_for_non_credit_cards
        self.ttl = ttl
        self.maximum_split_payment_count = maximum_split_payment_count
        self.items = items
        self.additional_params = additional_params
