from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.generate_bkm_express_token import BkmExpressGenerateTokenRequest
from craftgate.request_options import RequestOptions
from craftgate.response.generate_bkm_express_token_response import BkmExpressGenerateTokenResponse


class BkmExpressPaymentAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(BkmExpressPaymentAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def generate_token(self, request: BkmExpressGenerateTokenRequest) -> BkmExpressGenerateTokenResponse:
        path = "/payment/v2/bkm-express/generate-token"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=BkmExpressGenerateTokenResponse
        )
