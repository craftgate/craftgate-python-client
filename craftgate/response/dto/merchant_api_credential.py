from typing import Optional


class MerchantApiCredential(object):
    def __init__(
            self,
            name: Optional[str] = None,
            api_key: Optional[str] = None,
            secret_key: Optional[str] = None
    ) -> None:
        self.name = name
        self.api_key = api_key
        self.secret_key = secret_key
