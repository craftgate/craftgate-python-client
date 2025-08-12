from typing import Optional


class CheckMasterpassUserRequest(object):
    def __init__(
            self,
            masterpass_gsm_number: Optional[str] = None
    ) -> None:
        self.masterpass_gsm_number = masterpass_gsm_number
