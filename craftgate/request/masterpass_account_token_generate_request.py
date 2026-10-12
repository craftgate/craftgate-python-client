from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class MasterpassAccountTokenGenerateRequest(BaseRequest):
    def __init__(
            self,
            msisdn: Optional[str] = None,
            user_id: Optional[str] = None
    ) -> None:
        self.msisdn = msisdn
        self.user_id = user_id
