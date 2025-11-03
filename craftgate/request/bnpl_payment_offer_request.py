from decimal import Decimal
from typing import List, Dict, Any, Optional

from craftgate.model.apm_type import ApmType
from craftgate.model.currency import Currency
from craftgate.request.dto.bnpl_payment_cart_item import BnplPaymentCartItem


class BnplPaymentOfferRequest(object):
    def __init__(
            self,
            apm_type: Optional[ApmType] = None,
            merchant_apm_id: Optional[int] = None,
            price: Optional[Decimal] = None,
            currency: Optional[Currency] = None,
            apm_order_id: Optional[str] = None,
            additional_params: Optional[Dict[str, Any]] = None,
            items: Optional[List[BnplPaymentCartItem]] = None
    ) -> None:
        self.apm_type = apm_type
        self.merchant_apm_id = merchant_apm_id
        self.price = price
        self.currency = currency
        self.apm_order_id = apm_order_id
        self.additional_params = additional_params
        self.items = items
