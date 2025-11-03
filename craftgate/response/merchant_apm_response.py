from typing import List, Optional

from craftgate.model.apm_type import ApmType
from craftgate.model.currency import Currency
from craftgate.model.status import Status


class MerchantApmResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            status: Optional[Status] = None,
            name: Optional[str] = None,
            apm_type: Optional[ApmType] = None,
            hostname: Optional[str] = None,
            supported_currencies: Optional[List[Currency]] = None
    ) -> None:
        self.id = id
        self.status = status
        self.name = name
        self.apm_type = apm_type
        self.hostname = hostname
        self.supported_currencies = supported_currencies
