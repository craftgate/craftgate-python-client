from typing import Optional

from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.response.merchant_apm_list_response import MerchantApmListResponse


class MerchantApmAdapter(BaseAdapter):
    def __init__(self, request_options) -> None:
        super(MerchantApmAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def retrieve_apms(self) -> Optional[MerchantApmListResponse]:
        path = "/merchant/v1/merchant-apms"
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=MerchantApmListResponse
        )
