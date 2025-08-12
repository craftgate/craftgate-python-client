from typing import Optional

from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.search_installments_request import SearchInstallmentsRequest
from craftgate.response.bin_number_response import BinNumberResponse
from craftgate.response.installment_list_response import InstallmentListResponse
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class InstallmentAdapter(BaseAdapter):
    def __init__(self, request_options) -> None:
        super(InstallmentAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def search_installments(self, request: SearchInstallmentsRequest) -> Optional[InstallmentListResponse]:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/installment/v1/installments" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=InstallmentListResponse
        )

    def retrieve_bin_number(self, bin_number: str) -> Optional[BinNumberResponse]:
        path = "/installment/v1/bins/{}".format(bin_number)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=BinNumberResponse
        )
