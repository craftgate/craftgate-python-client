from typing import Optional


class MasterpassRetrieveLoyaltiesRequest(object):
    def __init__(
            self,
            msisdn: Optional[str] = None,
            bin_number: Optional[str] = None,
            card_name: Optional[str] = None,
            masterpassIntegrationVersion: Optional[int] = None
    ) -> None:
        self.msisdn = msisdn
        self.bin_number = bin_number
        self.card_name = card_name
        self.masterpassIntegrationVersion = masterpassIntegrationVersion
