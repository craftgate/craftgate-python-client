from typing import Optional

from craftgate.model.loyalty_type import LoyaltyType
from craftgate.request.common.base_request import BaseRequest
from craftgate.request.dto.fraud_check_parameters import FraudCheckParameters


class RetrieveLoyaltiesRequest(BaseRequest):
    def __init__(
            self,
            card_number: Optional[str] = None,
            expire_year: Optional[str] = None,
            expire_month: Optional[str] = None,
            cvc: Optional[str] = None,
            installment: Optional[int] = None,
            loyalty_type: Optional[LoyaltyType] = None,
            card_user_key: Optional[str] = None,
            card_token: Optional[str] = None,
            client_ip: Optional[str] = None,
            conversation_id: Optional[str] = None,
            fraud_params: Optional[FraudCheckParameters] = None,
    ) -> None:
        self.card_number = card_number
        self.expire_year = expire_year
        self.expire_month = expire_month
        self.cvc = cvc
        self.installment = installment
        self.loyalty_type = loyalty_type
        self.card_user_key = card_user_key
        self.card_token = card_token
        self.client_ip = client_ip
        self.conversation_id = conversation_id
        self.fraud_params = fraud_params
