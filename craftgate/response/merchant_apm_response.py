from typing import List, Optional
from craftgate.model.status import Status
from craftgate.model.apm_type import ApmType
from craftgate.model.currency import Currency


class MerchantApmResponse(object):
    def __init__(
        self,
        id=None,  # type: Optional[int]
        status=None,  # type: Optional[Status]
        name=None,  # type: Optional[str]
        apm_type=None,  # type: Optional[ApmType]
        hostname=None,  # type: Optional[str]
        supported_currencies=None  # type: Optional[List[Currency]]
    ):
        self.id = id
        self.status = status
        self.name = name
        self.apm_type = apm_type
        self.hostname = hostname
        self.supported_currencies = supported_currencies