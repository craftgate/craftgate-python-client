from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.model.fraud_check_status import FraudCheckStatus
from craftgate.model.fraud_value_type import FraudValueType
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.fraud_add_card_fingerprint_to_list_request import FraudAddCardFingerprintToListRequest
from craftgate.request.fraud_value_list_request import FraudValueListRequest
from craftgate.request.search_fraud_checks_request import SearchFraudChecksRequest
from craftgate.request.update_fraud_check_request import UpdateFraudCheckRequest
from craftgate.request_options import RequestOptions
from craftgate.response.fraud_all_value_lists_response import FraudAllValueListsResponse
from craftgate.response.fraud_check_list_response import FraudCheckListResponse
from craftgate.response.fraud_value_list_response import FraudValueListResponse
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class FraudAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(FraudAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def search_fraud_checks(self, request: SearchFraudChecksRequest) -> FraudCheckListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/fraud/v1/fraud-checks" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=FraudCheckListResponse
        )

    def update_fraud_check_status(self, id: int, fraud_check_status: FraudCheckStatus) -> None:
        path = "/fraud/v1/fraud-checks/{}/check-status".format(id)
        body = UpdateFraudCheckRequest(check_status=fraud_check_status)
        headers = self._create_headers(body, path)
        self._http_client.request(
            method="PUT",
            url=self.request_options.base_url + path,
            headers=headers,
            body=body,
            response_type=None
        )

    def retrieve_all_value_lists(self) -> FraudAllValueListsResponse:
        path = "/fraud/v1/value-lists/all"
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=FraudAllValueListsResponse
        )

    def retrieve_value_list(self, list_name: str) -> FraudValueListResponse:
        path = "/fraud/v1/value-lists/{}".format(list_name)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=FraudValueListResponse
        )

    def create_value_list(self, list_name: str, value_type: FraudValueType) -> None:
        body = FraudValueListRequest(
            type=value_type,
            list_name=list_name,
            value=None,
            duration_in_seconds=None
        )
        self.add_value_to_value_list(body)

    def delete_value_list(self, list_name: str) -> None:
        path = "/fraud/v1/value-lists/{}".format(list_name)
        headers = self._create_headers(None, path)
        self._http_client.request(
            method="DELETE",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=None
        )

    def add_value_to_value_list(self, request: FraudValueListRequest) -> None:
        path = "/fraud/v1/value-lists"
        headers = self._create_headers(request, path)
        self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=None
        )

    def add_card_fingerprint(self, request: FraudAddCardFingerprintToListRequest, list_name: str) -> None:
        path = "/fraud/v1/value-lists/{}/card-fingerprints".format(list_name)
        headers = self._create_headers(request, path)
        self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=None
        )

    def add_card_fingerprint_to_value_list(
            self, list_name: str, request: FraudAddCardFingerprintToListRequest
    ) -> None:
        """
        Deprecated: use add_card_fingerprint(request, list_name) instead.
        """
        self.add_card_fingerprint(request=request, list_name=list_name)

    def remove_value_from_value_list(self, list_name: str, value_id: str) -> None:
        path = "/fraud/v1/value-lists/{}/values/{}".format(list_name, value_id)
        headers = self._create_headers(None, path)
        self._http_client.request(
            method="DELETE",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=None
        )
