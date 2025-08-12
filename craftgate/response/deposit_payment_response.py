from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.fraud_action import FraudAction
from craftgate.model.payment_status import PaymentStatus
from craftgate.model.payment_type import PaymentType
from craftgate.response.dto.wallet_transaction import WalletTransaction


class DepositPaymentResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            price: Optional[Decimal] = None,
            currency: Optional[str] = None,
            buyer_member_id: Optional[int] = None,
            conversation_id: Optional[str] = None,
            bank_commission_rate: Optional[Decimal] = None,
            bank_commission_rate_amount: Optional[Decimal] = None,
            auth_code: Optional[str] = None,
            host_reference: Optional[str] = None,
            trans_id: Optional[str] = None,
            order_id: Optional[str] = None,
            payment_type: Optional[PaymentType] = None,
            created_date: Optional[datetime] = None,
            payment_status: Optional[PaymentStatus] = None,
            card_user_key: Optional[str] = None,
            card_token: Optional[str] = None,
            wallet_transaction: Optional[WalletTransaction] = None,
            fraud_id: Optional[int] = None,
            fraud_action: Optional[FraudAction] = None
    ) -> None:
        self.id = id
        self.price = price
        self.currency = currency
        self.buyer_member_id = buyer_member_id
        self.conversation_id = conversation_id
        self.bank_commission_rate = bank_commission_rate
        self.bank_commission_rate_amount = bank_commission_rate_amount
        self.auth_code = auth_code
        self.host_reference = host_reference
        self.trans_id = trans_id
        self.order_id = order_id
        self.payment_type = payment_type
        self.created_date = created_date
        self.payment_status = payment_status
        self.card_user_key = card_user_key
        self.card_token = card_token
        self.wallet_transaction = wallet_transaction
        self.fraud_id = fraud_id
        self.fraud_action = fraud_action
