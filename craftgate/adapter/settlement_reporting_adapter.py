from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.search_payout_bounced_transactions_request import SearchPayoutBouncedTransactionsRequest
from craftgate.request.search_payout_completed_transactions_request import SearchPayoutCompletedTransactionsRequest
from craftgate.request.search_payout_rows_request import SearchPayoutRowsRequest
from craftgate.response.payout_bounced_transaction_list_response import PayoutBouncedTransactionListResponse
from craftgate.response.payout_completed_transaction_list_response import PayoutCompletedTransactionListResponse
from craftgate.response.payout_detail_response import PayoutDetailResponse
from craftgate.response.payout_row_list_response import PayoutRowListResponse
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class SettlementReportingAdapter(BaseAdapter):
    def __init__(self, request_options):
        super(SettlementReportingAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def search_payout_completed_transactions(self, request):
        # type: (SearchPayoutCompletedTransactionsRequest) -> PayoutCompletedTransactionListResponse
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/settlement-reporting/v2/settlement-file/payout-completed-transactions" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PayoutCompletedTransactionListResponse
        )

    def search_bounced_payout_transactions(self, request):
        # type: (SearchPayoutBouncedTransactionsRequest) -> PayoutBouncedTransactionListResponse
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/settlement-reporting/v1/settlement-file/bounced-sub-merchant-rows" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PayoutBouncedTransactionListResponse
        )

    def retrieve_payout_details(self, id):
        # type: (int) -> PayoutDetailResponse
        path = "/settlement-reporting/v1/settlement-file/payout-details/{}".format(id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PayoutDetailResponse
        )

    def search_payout_rows(self, request):
        # type: (SearchPayoutRowsRequest) -> PayoutRowListResponse
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/settlement-reporting/v1/settlement-file-rows" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PayoutRowListResponse
        )
