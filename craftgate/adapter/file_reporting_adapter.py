from typing import Dict

from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.create_report_request import CreateReportRequest
from craftgate.request.retrieve_daily_payment_report_request import RetrieveDailyPaymentReportRequest
from craftgate.request.retrieve_daily_transaction_report_request import RetrieveDailyTransactionReportRequest
from craftgate.request.retrieve_report_request import RetrieveReportRequest
from craftgate.request_options import RequestOptions
from craftgate.response.report_demand_response import ReportDemandResponse
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class FileReportingAdapter(BaseAdapter):
    APPLICATION_OCTET_STREAM = "application/octet-stream"

    def __init__(self, request_options: RequestOptions) -> None:
        super().__init__(request_options)
        self._http_client = BaseHttpClient()

    def retrieve_daily_transaction_report(
            self, request: RetrieveDailyTransactionReportRequest
    ) -> bytes:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/file-reporting/v1/transaction-reports" + query
        headers = self._prepare_binary_headers(path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=bytes
        )

    def retrieve_daily_payment_report(
            self, request: RetrieveDailyPaymentReportRequest
    ) -> bytes:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/file-reporting/v1/payment-reports" + query
        headers = self._prepare_binary_headers(path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=bytes
        )

    def create_report(self, request: CreateReportRequest) -> ReportDemandResponse:
        path = "/file-reporting/v1/report-demands"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=ReportDemandResponse
        )

    def retrieve_report(self, request: RetrieveReportRequest, report_id: int) -> bytes:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/file-reporting/v1/reports/{}".format(report_id) + query
        headers = self._prepare_binary_headers(path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=bytes
        )

    def _prepare_binary_headers(self, path: str) -> Dict[str, str]:
        headers = self._create_headers(None, path)
        headers["Content-Type"] = self.APPLICATION_OCTET_STREAM
        return headers
