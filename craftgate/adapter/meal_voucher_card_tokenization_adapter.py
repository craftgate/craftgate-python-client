from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.init_meal_voucher_card_tokenization_request import InitMealVoucherCardTokenizationRequest
from craftgate.request.meal_voucher_card_tokenization_regenerate_request import \
    MealVoucherCardTokenizationRegenerateRequest
from craftgate.request.meal_voucher_card_tokenization_complete_request import \
    MealVoucherCardTokenizationCompleteRequest
from craftgate.request_options import RequestOptions
from craftgate.response.init_meal_voucher_card_tokenization_response import InitMealVoucherCardTokenizationResponse
from craftgate.response.meal_voucher_card_tokenization_complete_response import \
    MealVoucherCardTokenizationCompleteResponse


class MealVoucherCardTokenizationAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(MealVoucherCardTokenizationAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def init(self, request: InitMealVoucherCardTokenizationRequest) -> InitMealVoucherCardTokenizationResponse:
        path = "/payment/v1/meal-voucher/card-tokenizations/init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=InitMealVoucherCardTokenizationResponse
        )

    def regenerate(self, session_id: str, request: MealVoucherCardTokenizationRegenerateRequest) -> InitMealVoucherCardTokenizationResponse:
        path = f"/payment/v1/meal-voucher/card-tokenizations/{session_id}/regenerate"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=InitMealVoucherCardTokenizationResponse
        )

    def complete(self, session_id: str, request: MealVoucherCardTokenizationCompleteRequest) -> MealVoucherCardTokenizationCompleteResponse:
        path = f"/payment/v1/meal-voucher/card-tokenizations/{session_id}/complete"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=MealVoucherCardTokenizationCompleteResponse
        )
