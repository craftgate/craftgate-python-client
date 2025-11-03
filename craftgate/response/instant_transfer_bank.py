from typing import Optional


class InstantTransferBank(object):
    def __init__(
            self,
            bank_code: Optional[str] = None,
            bank_name: Optional[str] = None,
            bank_logo_url: Optional[str] = None
    ) -> None:
        self.bank_code = bank_code
        self.bank_name = bank_name
        self.bank_logo_url = bank_logo_url
