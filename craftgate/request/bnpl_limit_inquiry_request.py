from decimal import Decimal
from typing import Dict, List, Optional

from craftgate.model.apm_type import ApmType
from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.request.dto.payment_item import PaymentItem


class BnplLimitInquiryRequest(object):
    def __init__(
            self,
            apm_type: Optional[ApmType] = None,
            merchant_apm_id: Optional[int] = None,
            additional_params: Optional[Dict[str, str]] = None
    ) -> None:
        self.apm_type = apm_type
        self.merchant_apm_id = merchant_apm_id
        self.additional_params = additional_params
