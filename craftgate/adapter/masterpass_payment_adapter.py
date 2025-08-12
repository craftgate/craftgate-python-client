from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.check_masterpass_user_request import CheckMasterpassUserRequest
from craftgate.request.masterpass_payment_complete_request import MasterpassPaymentCompleteRequest
from craftgate.request.masterpass_payment_threeds_complete_request import MasterpassPaymentThreeDSCompleteRequest
from craftgate.request.masterpass_payment_threeds_init_request import MasterpassPaymentThreeDSInitRequest
from craftgate.request.masterpass_payment_token_generate_request import MasterpassPaymentTokenGenerateRequest
from craftgate.request.masterpass_retrieve_loyalties_request import MasterpassRetrieveLoyaltiesRequest
from craftgate.request_options import RequestOptions
from craftgate.response.check_masterpass_user_response import CheckMasterpassUserResponse
from craftgate.response.masterpass_payment_threeds_init_response import MasterpassPaymentThreeDSInitResponse
from craftgate.response.masterpass_payment_token_generate_response import MasterpassPaymentTokenGenerateResponse
from craftgate.response.payment_response import PaymentResponse
from craftgate.response.retrieve_loyalties_response import RetrieveLoyaltiesResponse


class MasterpassPaymentAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(MasterpassPaymentAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def check_masterpass_user(self, request: CheckMasterpassUserRequest) -> CheckMasterpassUserResponse:
        path = "/payment/v1/masterpass-payments/check-user"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=CheckMasterpassUserResponse
        )

    def generate_masterpass_payment_token(
            self, request: MasterpassPaymentTokenGenerateRequest
    ) -> MasterpassPaymentTokenGenerateResponse:
        path = "/payment/v2/masterpass-payments/generate-token"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=MasterpassPaymentTokenGenerateResponse
        )

    def complete_masterpass_payment(self, request: MasterpassPaymentCompleteRequest) -> PaymentResponse:
        path = "/payment/v2/masterpass-payments/complete"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentResponse
        )

    def init_3ds_masterpass_payment(
            self, request: MasterpassPaymentThreeDSInitRequest
    ) -> MasterpassPaymentThreeDSInitResponse:
        path = "/payment/v2/masterpass-payments/3ds-init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=MasterpassPaymentThreeDSInitResponse
        )

    def complete_3ds_masterpass_payment(
            self, request: MasterpassPaymentThreeDSCompleteRequest
    ) -> PaymentResponse:
        path = "/payment/v2/masterpass-payments/3ds-complete"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentResponse
        )

    def retrieve_loyalties(self, request: MasterpassRetrieveLoyaltiesRequest) -> RetrieveLoyaltiesResponse:
        path = "/payment/v2/masterpass-payments/loyalties/retrieve"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=RetrieveLoyaltiesResponse
        )
