from typing import List, Optional

from craftgate.response.dto.merchant_api_credential import MerchantApiCredential


class CreateMerchantResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            merchant_api_credentials: Optional[List[MerchantApiCredential]] = None
    ) -> None:
        self.id = id
        self.name = name
        self.merchant_api_credentials = merchant_api_credentials
