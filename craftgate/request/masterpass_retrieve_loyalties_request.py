from typing import Optional

class MasterpassRetrieveLoyaltiesRequest(object):
    def __init__(
        self,
        msisdn=None,         # type: Optional[str]
        bin_number=None,     # type: Optional[str]
        card_name=None       # type: Optional[str]
    ):
        self.msisdn = msisdn
        self.bin_number = bin_number
        self.card_name = card_name