from typing import List, Optional
from craftgate.response.dto.merchant_api_credential import MerchantApiCredential


class CreateMerchantResponse(object):
    def __init__(self, id=None, name=None, merchant_api_credentials=None):
        # type: (Optional[int], Optional[str], Optional[List[MerchantApiCredential]]) -> None
        self.id = id
        self.name = name
        self.merchant_api_credentials = merchant_api_credentials