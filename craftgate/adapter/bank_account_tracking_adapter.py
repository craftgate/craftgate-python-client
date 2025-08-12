from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.search_bank_account_tracking_records_request import SearchBankAccountTrackingRecordsRequest
from craftgate.request_options import RequestOptions
from craftgate.response.bank_account_tracking_record_list_response import BankAccountTrackingRecordListResponse
from craftgate.response.bank_account_tracking_record_response import BankAccountTrackingRecordResponse
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class BankAccountTrackingAdapter(BaseAdapter):

    def __init__(self, request_options: RequestOptions) -> None:
        super(BankAccountTrackingAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def search_records(
            self, request: SearchBankAccountTrackingRecordsRequest
    ) -> BankAccountTrackingRecordListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/bank-account-tracking/v1/merchant-bank-account-trackings/records" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=BankAccountTrackingRecordListResponse
        )

    def retrieve_record(self, id: int) -> BankAccountTrackingRecordResponse:
        path = "/bank-account-tracking/v1/merchant-bank-account-trackings/records/{}".format(id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=BankAccountTrackingRecordResponse
        )
