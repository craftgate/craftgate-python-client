from decimal import Decimal
from typing import Optional, Dict, Any

from craftgate.model.apm_type import ApmType
from craftgate.model.currency import Currency


class InitApmDepositPaymentRequest(object):
    def __init__(
            self,
            apm_type: Optional[ApmType] = None,
            merchant_apm_id: Optional[int] = None,
            price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            buyer_member_id: Optional[int] = None,
            payment_channel: Optional[str] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            callback_url: Optional[str] = None,
            apm_order_id: Optional[str] = None,
            apm_user_identity: Optional[str] = None,
            additional_params: Optional[Dict[str, Any]] = None,
            client_ip: Optional[str] = None
    ) -> None:
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
