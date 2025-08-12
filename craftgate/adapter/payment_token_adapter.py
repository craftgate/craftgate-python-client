from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.create_payment_token_request import CreatePaymentTokenRequest
from craftgate.request_options import RequestOptions
from craftgate.response.payment_token_response import PaymentTokenResponse


class PaymentTokenAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(PaymentTokenAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def create_payment_token(self, request: CreatePaymentTokenRequest) -> PaymentTokenResponse:
        path = "/payment/v1/payment-tokens"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentTokenResponse
        )

    def delete_payment_token(self, token: str) -> None:
        path = "/payment/v1/payment-tokens/{}".format(token)
        headers = self._create_headers(None, path)
        self._http_client.request(
            method="DELETE",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=None
        )
