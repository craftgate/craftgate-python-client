from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.create_member_request import CreateMemberRequest
from craftgate.request.create_merchant_request import CreateMerchantRequest
from craftgate.request.search_members_request import SearchMembersRequest
from craftgate.request.update_member_request import UpdateMemberRequest
from craftgate.request_options import RequestOptions
from craftgate.response.create_merchant_response import CreateMerchantResponse
from craftgate.response.member_list_response import MemberListResponse
from craftgate.response.member_response import MemberResponse
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class OnboardingAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(OnboardingAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def create_member(self, request: CreateMemberRequest) -> MemberResponse:
        path = "/onboarding/v1/members"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=MemberResponse
        )

    def update_member(self, member_id: int, request: UpdateMemberRequest) -> MemberResponse:
        path = "/onboarding/v1/members/{}".format(member_id)
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="PUT",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=MemberResponse
        )

    def retrieve_member(self, member_id: int) -> MemberResponse:
        path = "/onboarding/v1/members/{}".format(member_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=MemberResponse
        )

    def search_members(self, request: SearchMembersRequest) -> MemberListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/onboarding/v1/members{}".format(query)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=MemberListResponse
        )

    def create_merchant(self, request: CreateMerchantRequest) -> CreateMerchantResponse:
        path = "/onboarding/v1/merchants"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=CreateMerchantResponse
        )
