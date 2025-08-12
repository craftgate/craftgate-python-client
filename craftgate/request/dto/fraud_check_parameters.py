from typing import Optional


class FraudCheckParameters(object):
    def __init__(
            self,
            buyer_external_id: Optional[str] = None,
            buyer_phone_number: Optional[str] = None,
            buyer_email: Optional[str] = None,
            custom_fraud_variable: Optional[str] = None
    ) -> None:
        self.buyer_external_id = buyer_external_id
        self.buyer_phone_number = buyer_phone_number
        self.buyer_email = buyer_email
        self.custom_fraud_variable = custom_fraud_variable
