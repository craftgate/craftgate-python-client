from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.model.pos_status import PosStatus
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.create_merchant_pos_request import CreateMerchantPosRequest
from craftgate.request.search_merchant_pos_request import SearchMerchantPosRequest
from craftgate.request.update_merchant_pos_commissions_request import UpdateMerchantPosCommissionsRequest
from craftgate.request.update_merchant_pos_request import UpdateMerchantPosRequest
from craftgate.request_options import RequestOptions
from craftgate.response.merchant_pos_commission_list_response import MerchantPosCommissionListResponse
from craftgate.response.merchant_pos_list_response import MerchantPosListResponse
from craftgate.response.merchant_pos_response import MerchantPosResponse
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class MerchantAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(MerchantAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def create_merchant_pos(self, request: CreateMerchantPosRequest) -> MerchantPosResponse:
        path = "/merchant/v1/merchant-poses"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=MerchantPosResponse
        )

    def update_merchant_pos(self, merchant_pos_id: int, request: UpdateMerchantPosRequest) -> MerchantPosResponse:
        path = "/merchant/v1/merchant-poses/{}".format(merchant_pos_id)
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="PUT",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=MerchantPosResponse
        )

    def update_merchant_pos_status(self, merchant_pos_id: int, pos_status: PosStatus) -> None:
        path = "/merchant/v1/merchant-poses/{}/status/{}".format(merchant_pos_id, pos_status.name)
        headers = self._create_headers(None, path)
        self._http_client.request(
            method="PUT",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=None
        )

    def search_merchant_pos(self, request: SearchMerchantPosRequest) -> MerchantPosListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/merchant/v1/merchant-poses" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=MerchantPosListResponse
        )

    def retrieve(self, merchant_pos_id: int) -> MerchantPosResponse:
        path = "/merchant/v1/merchant-poses/{}".format(merchant_pos_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=MerchantPosResponse
        )

    def delete_merchant_pos(self, merchant_pos_id: int) -> None:
        path = "/merchant/v1/merchant-poses/{}".format(merchant_pos_id)
        headers = self._create_headers(None, path)
        self._http_client.request(
            method="DELETE",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=None
        )

    def retrieve_merchant_pos_commissions(self, merchant_pos_id: int) -> MerchantPosCommissionListResponse:
        path = "/merchant/v1/merchant-poses/{}/commissions".format(merchant_pos_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=MerchantPosCommissionListResponse
        )

    def update_merchant_pos_commissions(
            self, merchant_pos_id: int, request: UpdateMerchantPosCommissionsRequest
    ) -> MerchantPosCommissionListResponse:
        path = "/merchant/v1/merchant-poses/{}/commissions".format(merchant_pos_id)
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=MerchantPosCommissionListResponse
        )
