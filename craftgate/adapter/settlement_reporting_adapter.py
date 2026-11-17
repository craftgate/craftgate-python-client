from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.search_payment_transaction_payouts_request import SearchPaymentTransactionPayoutsRequest
from craftgate.request.search_payout_bounced_transactions_request import SearchPayoutBouncedTransactionsRequest
from craftgate.request.search_payout_completed_items_request import SearchPayoutCompletedItemsRequest
from craftgate.request.search_payout_rows_request import SearchPayoutRowsRequest
from craftgate.request_options import RequestOptions
from craftgate.response.payment_tx_payout_list_response import PaymentTxPayoutListResponse
from craftgate.response.payment_tx_payout_response import PaymentTxPayoutResponse
from craftgate.response.payout_bounced_transaction_list_response import PayoutBouncedTransactionListResponse
from craftgate.response.payout_completed_item_list_response import PayoutCompletedItemListResponse
from craftgate.response.payout_row_list_response import PayoutRowListResponse
from craftgate.response.settlement_row_response import SettlementRowResponse
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class SettlementReportingAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(SettlementReportingAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def search_payout_completed_items(
            self, request: SearchPayoutCompletedItemsRequest
    ) -> PayoutCompletedItemListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/settlement-reporting/v1/settlement-file/payout-completed-items" + query
        headers = self._create_headers_without_body(request, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PayoutCompletedItemListResponse
        )

    def search_bounced_payout_transactions(
            self, request: SearchPayoutBouncedTransactionsRequest
    ) -> PayoutBouncedTransactionListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/settlement-reporting/v1/settlement-file/bounced-sub-merchant-rows" + query
        headers = self._create_headers_without_body(request, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PayoutBouncedTransactionListResponse
        )

    def retrieve_settlement_row(self, settlement_row_id: int) -> SettlementRowResponse:
        path = "/settlement-reporting/v1/settlement-file/rows/{}".format(settlement_row_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=SettlementRowResponse
        )

    def search_payout_rows(self, request: SearchPayoutRowsRequest) -> PayoutRowListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/settlement-reporting/v1/settlement-file-rows" + query
        headers = self._create_headers_without_body(request, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PayoutRowListResponse
        )

    def retrieve_payment_transaction_payout(self, payment_transaction_id: int) -> PaymentTxPayoutResponse:
        path = "/settlement-reporting/v1/payment-transactions/{}/payout".format(payment_transaction_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PaymentTxPayoutResponse
        )

    def search_payment_transaction_payouts(
            self, request: SearchPaymentTransactionPayoutsRequest
    ) -> PaymentTxPayoutListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/settlement-reporting/v1/payment-transactions/payouts" + query
        headers = self._create_headers_without_body(request, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PaymentTxPayoutListResponse
        )
