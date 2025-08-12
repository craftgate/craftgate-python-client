from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.create_instant_wallet_settlement_request import CreateInstantWalletSettlementRequest
from craftgate.request.create_payout_account_request import CreatePayoutAccountRequest
from craftgate.request.search_payout_account_request import SearchPayoutAccountRequest
from craftgate.request.update_payout_account_request import UpdatePayoutAccountRequest
from craftgate.response.payout_account_list_response import PayoutAccountListResponse
from craftgate.response.payout_account_response import PayoutAccountResponse
from craftgate.response.settlement_response import SettlementResponse
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class SettlementAdapter(BaseAdapter):
    def __init__(self, request_options):
        super(SettlementAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def create_instant_wallet_settlement(self, request):
        # type: (CreateInstantWalletSettlementRequest) -> SettlementResponse
        path = "/settlement/v1/instant-wallet-settlements"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=SettlementResponse
        )

    def create_payout_account(self, request):
        # type: (CreatePayoutAccountRequest) -> PayoutAccountResponse
        path = "/settlement/v1/payout-accounts"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PayoutAccountResponse
        )

    def update_payout_account(self, id, request):
        # type: (int, UpdatePayoutAccountRequest) -> None
        path = "/settlement/v1/payout-accounts/{}".format(id)
        headers = self._create_headers(request, path)
        self._http_client.request(
            method="PUT",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=None
        )

    def delete_payout_account(self, id):
        # type: (int) -> None
        path = "/settlement/v1/payout-accounts/{}".format(id)
        headers = self._create_headers(None, path)
        self._http_client.request(
            method="DELETE",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=None
        )

    def search_payout_account(self, request):
        # type: (SearchPayoutAccountRequest) -> PayoutAccountListResponse
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/settlement/v1/payout-accounts" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PayoutAccountListResponse
        )
