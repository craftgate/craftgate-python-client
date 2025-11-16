from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.search_payment_refunds_request import SearchPaymentRefundsRequest
from craftgate.request.search_payment_transaction_refunds_request import SearchPaymentTransactionRefundsRequest
from craftgate.request.search_payments_request import SearchPaymentsRequest
from craftgate.request_options import RequestOptions
from craftgate.response.reporting_payment_list_response import ReportingPaymentListResponse
from craftgate.response.reporting_payment_refund_list_response import ReportingPaymentRefundListResponse
from craftgate.response.reporting_payment_response import ReportingPaymentResponse
from craftgate.response.reporting_payment_transaction_list_response import ReportingPaymentTransactionListResponse
from craftgate.response.reporting_payment_transaction_refund_list_response import (
    ReportingPaymentTransactionRefundListResponse,
)
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class PaymentReportingAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(PaymentReportingAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def search_payments(self, request: SearchPaymentsRequest) -> ReportingPaymentListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/payment-reporting/v1/payments" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=ReportingPaymentListResponse,
        )

    def retrieve_payment(self, payment_id: int) -> ReportingPaymentResponse:
        path = "/payment-reporting/v1/payments/{}".format(payment_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=ReportingPaymentResponse,
        )

    def retrieve_payment_transactions(self, payment_id: int) -> ReportingPaymentTransactionListResponse:
        path = "/payment-reporting/v1/payments/{}/transactions".format(payment_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=ReportingPaymentTransactionListResponse,
        )

    def retrieve_payment_refunds(self, payment_id: int) -> ReportingPaymentRefundListResponse:
        path = "/payment-reporting/v1/payments/{}/refunds".format(payment_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=ReportingPaymentRefundListResponse,
        )

    def retrieve_payment_transaction_refunds(
            self, payment_id: int, payment_transaction_id: int
    ) -> ReportingPaymentTransactionRefundListResponse:
        path = "/payment-reporting/v1/payments/{}/transactions/{}/refunds".format(payment_id, payment_transaction_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=ReportingPaymentTransactionRefundListResponse,
        )

    def search_payment_refunds(self, request: SearchPaymentRefundsRequest) -> ReportingPaymentRefundListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/payment-reporting/v1/refunds" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=ReportingPaymentRefundListResponse,
        )

    def search_payment_transaction_refunds(
            self, request: SearchPaymentTransactionRefundsRequest
    ) -> ReportingPaymentTransactionRefundListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/payment-reporting/v1/refund-transactions" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=ReportingPaymentTransactionRefundListResponse,
        )
