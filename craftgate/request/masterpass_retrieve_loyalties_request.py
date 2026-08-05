from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class MasterpassRetrieveLoyaltiesRequest(BaseRequest):
    def __init__(
            self,
            msisdn: Optional[str] = None,
            bin_number: Optional[str] = None,
            card_name: Optional[str] = None,
            masterpass_integration_version: Optional[int] = None
    ) -> None:
        self.msisdn = msisdn
        self.bin_number = bin_number
        self.card_name = card_name
        self.masterpass_integration_version = masterpass_integration_version
