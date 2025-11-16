from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.create_product_request import CreateProductRequest
from craftgate.request.search_products_request import SearchProductsRequest
from craftgate.request.update_product_request import UpdateProductRequest
from craftgate.request_options import RequestOptions
from craftgate.response.product_list_response import ProductListResponse
from craftgate.response.product_response import ProductResponse
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class PayByLinkAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(PayByLinkAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def create_product(self, request: CreateProductRequest) -> ProductResponse:
        path = "/craftlink/v1/products"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=ProductResponse
        )

    def update_product(self, product_id: int, request: UpdateProductRequest) -> ProductResponse:
        path = "/craftlink/v1/products/{}".format(product_id)
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="PUT",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=ProductResponse
        )

    def retrieve_product(self, product_id: int) -> ProductResponse:
        path = "/craftlink/v1/products/{}".format(product_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=ProductResponse
        )

    def delete_product(self, product_id: int) -> None:
        path = "/craftlink/v1/products/{}".format(product_id)
        headers = self._create_headers(None, path)
        self._http_client.request(
            method="DELETE",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=None
        )

    def search_products(self, request: SearchProductsRequest) -> ProductListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/craftlink/v1/products{}".format(query)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=ProductListResponse
        )
