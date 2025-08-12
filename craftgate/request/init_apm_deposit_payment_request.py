from typing import Optional, Dict, Any
from craftgate.model.apm_type import ApmType
from craftgate.model.currency import Currency

class InitApmDepositPaymentRequest(object):
    def __init__(self,
                 apm_type=None,                # type: Optional[ApmType]
                 merchant_apm_id=None,         # type: Optional[int]
                 price=None,                   # type: Optional[float]
                 currency=None,                # type: Optional[Currency]
                 buyer_member_id=None,         # type: Optional[int]
                 payment_channel=None,         # type: Optional[str]
                 conversation_id=None,         # type: Optional[str]
                 external_id=None,             # type: Optional[str]
                 callback_url=None,            # type: Optional[str]
                 apm_order_id=None,             # type: Optional[str]
                 apm_user_identity=None,        # type: Optional[str]
                 additional_params=None,        # type: Optional[Dict[str, Any]]
                 client_ip=None                 # type: Optional[str]
                 ):
        self.apm_type = apm_type
        self.merchant_apm_id = merchant_apm_id
        self.price = price
        self.currency = currency
        self.buyer_member_id = buyer_member_id
        self.payment_channel = payment_channel
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.callback_url = callback_url
        self.apm_order_id = apm_order_id
        self.apm_user_identity = apm_user_identity
        self.additional_params = additional_params
        self.client_ip = client_ip