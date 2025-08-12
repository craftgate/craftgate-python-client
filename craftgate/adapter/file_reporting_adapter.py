from typing import Optional

from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.retrieve_daily_payment_report_request import RetrieveDailyPaymentReportRequest
from craftgate.request.retrieve_daily_transaction_report_request import RetrieveDailyTransactionReportRequest
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class FileReportingAdapter(BaseAdapter):
    APPLICATION_OCTET_STREAM = "application/octet-stream"

    def __init__(self, request_options):
        super().__init__(request_options)
        self._http_client = BaseHttpClient()

    def retrieve_daily_transaction_report(
            self, request: RetrieveDailyTransactionReportRequest
    ) -> Optional[bytes]:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/file-reporting/v1/transaction-reports" + query
        headers = self._create_headers(None, path)
        headers["Content-Type"] = self.APPLICATION_OCTET_STREAM
        return self._http_client.request("GET", self.request_options.base_url + path, headers, None, bytes)

    def retrieve_daily_payment_report(
            self, request: RetrieveDailyPaymentReportRequest
    ) -> Optional[bytes]:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/file-reporting/v1/payment-reports" + query
        headers = self._create_headers(None, path)
        headers["Content-Type"] = self.APPLICATION_OCTET_STREAM
        return self._http_client.request("GET", self.request_options.base_url + path, headers, None, bytes)
