from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.card_association import CardAssociation
from craftgate.model.card_type import CardType
from craftgate.model.currency import Currency
from craftgate.model.fraud_action import FraudAction
from craftgate.model.loyalty import Loyalty
from craftgate.model.payment_group import PaymentGroup
from craftgate.model.payment_phase import PaymentPhase
from craftgate.model.payment_provider import PaymentProvider
from craftgate.model.payment_source import PaymentSource
from craftgate.model.payment_status import PaymentStatus
from craftgate.model.payment_type import PaymentType
from craftgate.response.dto.merchant_pos import MerchantPos
from craftgate.response.dto.payment_error import PaymentError


class BasePaymentResponse:
    def __init__(
            self,
            id: Optional[int] = None,
            created_date: Optional[datetime] = None,
            price: Optional[Decimal] = None,
            paid_price: Optional[Decimal] = None,
            wallet_price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            buyer_member_id: Optional[int] = None,
            installment: Optional[int] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            payment_type: Optional[PaymentType] = None,
            payment_provider: Optional[PaymentProvider] = None,
            payment_source: Optional[PaymentSource] = None,
            payment_group: Optional[PaymentGroup] = None,
            payment_status: Optional[PaymentStatus] = None,
            payment_phase: Optional[PaymentPhase] = None,
            payment_channel: Optional[str] = None,
            is_three_ds: Optional[bool] = None,
            merchant_commission_rate: Optional[Decimal] = None,
            merchant_commission_rate_amount: Optional[Decimal] = None,
            bank_commission_rate: Optional[Decimal] = None,
            bank_commission_rate_amount: Optional[Decimal] = None,
            paid_with_stored_card: Optional[bool] = None,
            bin_number: Optional[str] = None,
            last_four_digits: Optional[str] = None,
            auth_code: Optional[str] = None,
            host_reference: Optional[str] = None,
            trans_id: Optional[str] = None,
            md_status: Optional[int] = None,
            order_id: Optional[str] = None,
            card_holder_name: Optional[str] = None,
            bank_card_holder_name: Optional[str] = None,
            card_issuer_bank_name: Optional[str] = None,
            card_issuer_bank_id: Optional[int] = None,
            card_type: Optional[CardType] = None,
            card_association: Optional[CardAssociation] = None,
            card_brand: Optional[str] = None,
            requested_pos_alias: Optional[str] = None,
            blockage_resolved_date: Optional[datetime] = None,
            fraud_id: Optional[int] = None,
            fraud_action: Optional[FraudAction] = None,
            fraud_score: Optional[float] = None,
            pos: Optional[MerchantPos] = None,
            loyalty: Optional[Loyalty] = None,
            payment_error: Optional[PaymentError] = None
    ) -> None:
        self.id = id
        self.created_date = created_date
        self.price = price
        self.paid_price = paid_price
        self.wallet_price = wallet_price
        self.currency = currency
        self.buyer_member_id = buyer_member_id
        self.installment = installment
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.payment_type = payment_type
        self.payment_provider = payment_provider
        self.payment_source = payment_source
        self.payment_group = payment_group
        self.payment_status = payment_status
        self.payment_phase = payment_phase
        self.payment_channel = payment_channel
        self.is_three_ds = is_three_ds
        self.merchant_commission_rate = merchant_commission_rate
        self.merchant_commission_rate_amount = merchant_commission_rate_amount
        self.bank_commission_rate = bank_commission_rate
        self.bank_commission_rate_amount = bank_commission_rate_amount
        self.paid_with_stored_card = paid_with_stored_card
        self.bin_number = bin_number
        self.last_four_digits = last_four_digits
        self.auth_code = auth_code
        self.host_reference = host_reference
        self.trans_id = trans_id
        self.md_status = md_status
        self.order_id = order_id
        self.card_holder_name = card_holder_name
        self.bank_card_holder_name = bank_card_holder_name
        self.card_issuer_bank_name = card_issuer_bank_name
        self.card_issuer_bank_id = card_issuer_bank_id
        self.card_type = card_type
        self.card_association = card_association
        self.card_brand = card_brand
        self.requested_pos_alias = requested_pos_alias
        self.blockage_resolved_date = blockage_resolved_date
        self.fraud_id = fraud_id
        self.fraud_action = fraud_action
        self.fraud_score = fraud_score
        self.pos = pos
        self.loyalty = loyalty
        self.payment_error = payment_error
