from typing import Optional

class InstantTransferBank(object):
    def __init__(
        self,
        bank_code=None,      # type: Optional[str]
        bank_name=None,      # type: Optional[str]
        bank_logo_url=None   # type: Optional[str]
    ):
        self.bank_code = bank_code
        self.bank_name = bank_name
        self.bank_logo_url = bank_logo_url