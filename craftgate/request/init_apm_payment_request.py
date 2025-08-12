from decimal import Decimal
from typing import Dict, List, Optional

from craftgate.model.apm_type import ApmType
from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.request.dto.payment_item import PaymentItem


class InitApmPaymentRequest(object):
    def __init__(
            self,
            apm_type: Optional[ApmType] = None,
            merchant_apm_id: Optional[int] = None,
            price: Optional[Decimal] = None,
            paid_price: Optional[Decimal] = None,
            buyer_member_id: Optional[int] = None,
            currency: Optional[Currency] = None,
            payment_group: Optional[PaymentGroup] = None,
            payment_channel: Optional[str] = None,
            conversation_id: Optional[str] = None,
            external_id: Optional[str] = None,
            callback_url: Optional[str] = None,
            apm_order_id: Optional[str] = None,
            apm_user_identity: Optional[str] = None,
            additional_params: Optional[Dict[str, str]] = None,
            client_ip: Optional[str] = None,
            items: Optional[List[PaymentItem]] = None
    ) -> None:
        self.apm_type = apm_type
        self.merchant_apm_id = merchant_apm_id
        self.price = price
        self.paid_price = paid_price
        self.buyer_member_id = buyer_member_id
        self.currency = currency
        self.payment_group = payment_group
        self.payment_channel = payment_channel
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.callback_url = callback_url
        self.apm_order_id = apm_order_id
        self.apm_user_identity = apm_user_identity
        self.additional_params = additional_params
        self.client_ip = client_ip
        self.items = items
