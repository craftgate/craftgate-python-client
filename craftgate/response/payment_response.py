from typing import Optional, List, Dict, Any

from craftgate.response.common.base_payment_response import BasePaymentResponse
from craftgate.response.dto.payment_transaction import PaymentTransaction


class PaymentResponse(BasePaymentResponse):
    def __init__(
        self,
        card_user_key: Optional[str] = None,
        card_token: Optional[str] = None,
        additional_data: Optional[Dict[str, Any]] = None,
        payment_transactions: Optional[List[PaymentTransaction]] = None,
        **kwargs
    ) -> None:
        super(PaymentResponse, self).__init__(**kwargs)
        self.card_user_key = card_user_key
        self.card_token = card_token
        self.additional_data = additional_data
        self.payment_transactions = payment_transactions
