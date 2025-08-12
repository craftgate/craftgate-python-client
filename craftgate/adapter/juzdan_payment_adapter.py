from typing import Optional

from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.init_juzdan_payment_request import InitJuzdanPaymentRequest
from craftgate.response.init_juzdan_payment_response import InitJuzdanPaymentResponse
from craftgate.response.payment_response import PaymentResponse


class JuzdanPaymentAdapter(BaseAdapter):
    def __init__(self, request_options) -> None:
        super(JuzdanPaymentAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def init(self, request: InitJuzdanPaymentRequest) -> Optional[InitJuzdanPaymentResponse]:
        path = "/payment/v1/juzdan-payments/init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=InitJuzdanPaymentResponse
        )

    def retrieve(self, reference_id: str) -> Optional[PaymentResponse]:
        path = "/payment/v1/juzdan-payments/{}".format(reference_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PaymentResponse
        )
