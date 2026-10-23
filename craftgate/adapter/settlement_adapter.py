from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.create_instant_wallet_settlement_request import CreateInstantWalletSettlementRequest
from craftgate.request_options import RequestOptions
from craftgate.response.settlement_response import SettlementResponse


class SettlementAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(SettlementAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def create_instant_wallet_settlement(self, request: CreateInstantWalletSettlementRequest) -> SettlementResponse:
        path = "/settlement/v1/instant-wallet-settlements"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=SettlementResponse
        )
