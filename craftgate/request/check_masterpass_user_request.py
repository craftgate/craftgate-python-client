from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class CheckMasterpassUserRequest(BaseRequest):
    def __init__(
            self,
            masterpass_gsm_number: Optional[str] = None
    ) -> None:
        self.masterpass_gsm_number = masterpass_gsm_number
