from typing import Optional
from decimal import Decimal
from datetime import datetime
from craftgate.model.payment_type import PaymentType
from craftgate.model.payment_status import PaymentStatus
from craftgate.model.fraud_action import FraudAction
from craftgate.response.dto.wallet_transaction import WalletTransaction

class DepositPaymentResponse(object):
    def __init__(
        self,
        id=None,                            # type: Optional[int]
        price=None,                         # type: Optional[Decimal]
        currency=None,                       # type: Optional[str]
        buyer_member_id=None,                # type: Optional[int]
        conversation_id=None,                # type: Optional[str]
        bank_commission_rate=None,           # type: Optional[Decimal]
        bank_commission_rate_amount=None,    # type: Optional[Decimal]
        auth_code=None,                       # type: Optional[str]
        host_reference=None,                  # type: Optional[str]
        trans_id=None,                        # type: Optional[str]
        order_id=None,                        # type: Optional[str]
        payment_type=None,                    # type: Optional[PaymentType]
        created_date=None,                    # type: Optional[datetime]
        payment_status=None,                  # type: Optional[PaymentStatus]
        card_user_key=None,                   # type: Optional[str]
        card_token=None,                      # type: Optional[str]
        wallet_transaction=None,              # type: Optional[WalletTransaction]
        fraud_id=None,                         # type: Optional[int]
        fraud_action=None                      # type: Optional[FraudAction]
    ):
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