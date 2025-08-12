from typing import List, Dict, Any, Optional

from craftgate.model.apm_type import ApmType
from craftgate.model.currency import Currency
from craftgate.request.dto.bnpl_payment_cart_item import BnplPaymentCartItem


class BnplPaymentOfferRequest(object):
    def __init__(self,
                 apm_type=None,  # type: Optional[ApmType]
                 merchant_apm_id=None,  # type: Optional[int]
                 price=None,  # type: Optional[float]
                 currency=None,  # type: Optional[Currency]
                 apm_order_id=None,  # type: Optional[str]
                 additional_params=None,  # type: Optional[Dict[str, Any]]
                 items=None  # type: Optional[List[BnplPaymentCartItem]]
                 ):
        self.apm_type = apm_type
        self.merchant_apm_id = merchant_apm_id
        self.price = price
        self.currency = currency
        self.apm_order_id = apm_order_id
        self.additional_params = additional_params or {}
        self.items = items or []
