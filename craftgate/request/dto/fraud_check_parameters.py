from typing import Optional


class FraudCheckParameters(object):
    def __init__(self,
                 buyer_external_id=None,  # type: Optional[str]
                 buyer_phone_number=None,  # type: Optional[str]
                 buyer_email=None,  # type: Optional[str]
                 custom_fraud_variable=None  # type: Optional[str]
                 ):
        self.buyer_external_id = buyer_external_id
        self.buyer_phone_number = buyer_phone_number
        self.buyer_email = buyer_email
        self.custom_fraud_variable = custom_fraud_variable
