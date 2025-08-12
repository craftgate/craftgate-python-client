from typing import Optional

from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.complete_bkm_express_request import CompleteBkmExpressRequest
from craftgate.request.init_bkm_express_request import InitBkmExpressRequest
from craftgate.request_options import RequestOptions
from craftgate.response.init_bkm_express_response import InitBkmExpressResponse
from craftgate.response.payment_response import PaymentResponse


class BkmExpressPaymentAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(BkmExpressPaymentAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def init(self, request: InitBkmExpressRequest) -> Optional[InitBkmExpressResponse]:
        path = "/payment/v1/bkm-express/init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=InitBkmExpressResponse
        )

    def complete(self, request: CompleteBkmExpressRequest) -> Optional[PaymentResponse]:
        path = "/payment/v1/bkm-express/complete"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentResponse
        )

    def retrieve_payment(self, ticket_id: str) -> Optional[PaymentResponse]:
        path = "/payment/v1/bkm-express/payments/{}".format(ticket_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PaymentResponse
        )

    def retrieve_payment_by_token(self, token: str) -> Optional[PaymentResponse]:
        path = "/payment/v1/bkm-express/{}".format(token)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PaymentResponse
        )
