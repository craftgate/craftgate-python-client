from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.apple_pay_merchant_session_create_request import ApplePayMerchantSessionCreateRequest
from craftgate.request.approve_payment_transactions_request import ApprovePaymentTransactionsRequest
from craftgate.request.bnpl_payment_offer_request import BnplPaymentOfferRequest
from craftgate.request.clone_card_request import CloneCardRequest
from craftgate.request.complete_apm_payment_request import CompleteApmPaymentRequest
from craftgate.request.complete_pos_apm_payment_request import CompletePosApmPaymentRequest
from craftgate.request.complete_three_ds_payment_request import CompleteThreeDSPaymentRequest
from craftgate.request.create_apm_payment_request import CreateApmPaymentRequest
from craftgate.request.create_deposit_payment_request import CreateDepositPaymentRequest
from craftgate.request.create_fund_transfer_deposit_payment_request import CreateFundTransferDepositPaymentRequest
from craftgate.request.create_payment_request import CreatePaymentRequest
from craftgate.request.delete_stored_card_request import DeleteStoredCardRequest
from craftgate.request.disapprove_payment_transactions_request import DisapprovePaymentTransactionsRequest
from craftgate.request.init_apm_deposit_payment_request import InitApmDepositPaymentRequest
from craftgate.request.init_apm_payment_request import InitApmPaymentRequest
from craftgate.request.init_bnpl_payment_request import InitBnplPaymentRequest
from craftgate.request.init_checkout_card_verify_request import InitCheckoutCardVerifyRequest
from craftgate.request.init_checkout_payment_request import InitCheckoutPaymentRequest
from craftgate.request.init_garanti_pay_payment_request import InitGarantiPayPaymentRequest
from craftgate.request.init_pos_apm_payment_request import InitPosApmPaymentRequest
from craftgate.request.init_three_ds_payment_request import InitThreeDSPaymentRequest
from craftgate.request.post_auth_payment_request import PostAuthPaymentRequest
from craftgate.request.refund_payment_request import RefundPaymentRequest
from craftgate.request.refund_payment_transaction_mark_as_refunded_request import \
    RefundPaymentTransactionMarkAsRefundedRequest
from craftgate.request.refund_payment_transaction_request import RefundPaymentTransactionRequest
from craftgate.request.retrieve_loyalties_request import RetrieveLoyaltiesRequest
from craftgate.request.retrieve_provider_card_request import RetrieveProviderCardRequest
from craftgate.request.search_stored_cards_request import SearchStoredCardsRequest
from craftgate.request.store_card_request import StoreCardRequest
from craftgate.request.update_card_request import UpdateCardRequest
from craftgate.request.update_payment_transaction_request import UpdatePaymentTransactionRequest
from craftgate.request.verify_card_request import VerifyCardRequest
from craftgate.request_options import RequestOptions
from craftgate.response.apm_deposit_payment_response import ApmDepositPaymentResponse
from craftgate.response.apm_payment_complete_response import ApmPaymentCompleteResponse
from craftgate.response.apm_payment_init_response import ApmPaymentInitResponse
from craftgate.response.bnpl_payment_offer_response import BnplPaymentOfferResponse
from craftgate.response.bnpl_payment_verify_response import BnplPaymentVerifyResponse
from craftgate.response.deposit_payment_response import DepositPaymentResponse
from craftgate.response.fund_transfer_deposit_payment_response import FundTransferDepositPaymentResponse
from craftgate.response.init_bnpl_payment_response import InitBnplPaymentResponse
from craftgate.response.init_checkout_card_verify_response import InitCheckoutCardVerifyResponse
from craftgate.response.init_checkout_payment_response import InitCheckoutPaymentResponse
from craftgate.response.init_garanti_pay_payment_response import InitGarantiPayPaymentResponse
from craftgate.response.init_pos_apm_payment_response import InitPosApmPaymentResponse
from craftgate.response.init_three_ds_payment_response import InitThreeDSPaymentResponse
from craftgate.response.instant_transfer_banks_response import InstantTransferBanksResponse
from craftgate.response.multi_payment_response import MultiPaymentResponse
from craftgate.response.payment_refund_response import PaymentRefundResponse
from craftgate.response.payment_response import PaymentResponse
from craftgate.response.payment_transaction_approval_list_response import PaymentTransactionApprovalListResponse
from craftgate.response.payment_transaction_refund_list_response import PaymentTransactionRefundListResponse
from craftgate.response.payment_transaction_refund_response import PaymentTransactionRefundResponse
from craftgate.response.payment_transaction_response import PaymentTransactionResponse
from craftgate.response.retrieve_checkout_card_verify_response import RetrieveCheckoutCardVerifyResponse
from craftgate.response.retrieve_loyalties_response import RetrieveLoyaltiesResponse
from craftgate.response.stored_card_list_response import StoredCardListResponse
from craftgate.response.stored_card_response import StoredCardResponse
from craftgate.response.verify_card_response import VerifyCardResponse
from craftgate.utils.hash_generator import HashGenerator
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class PaymentAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(PaymentAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def create_payment(self, request: CreatePaymentRequest) -> PaymentResponse:
        path = "/payment/v1/card-payments"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentResponse
        )

    def retrieve_payment(self, payment_id: int) -> PaymentResponse:
        path = "/payment/v1/card-payments/{}".format(payment_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PaymentResponse
        )

    def init_3ds_payment(self, request: InitThreeDSPaymentRequest) -> InitThreeDSPaymentResponse:
        path = "/payment/v1/card-payments/3ds-init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=InitThreeDSPaymentResponse
        )

    def complete_3ds_payment(self, request: CompleteThreeDSPaymentRequest) -> PaymentResponse:
        path = "/payment/v1/card-payments/3ds-complete"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentResponse
        )

    def post_auth_payment(self, payment_id: int, request: PostAuthPaymentRequest) -> PaymentResponse:
        path = "/payment/v1/card-payments/{}/post-auth".format(payment_id)
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentResponse
        )

    def init_checkout_payment(self, request: InitCheckoutPaymentRequest) -> InitCheckoutPaymentResponse:
        path = "/payment/v1/checkout-payments/init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=InitCheckoutPaymentResponse
        )

    def init_checkout_card_verify(self, request: InitCheckoutCardVerifyRequest) -> InitCheckoutCardVerifyResponse:
        path = "/payment/v1/checkout-card-verify/init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=InitCheckoutCardVerifyResponse
        )

    def retrieve_checkout_card_verify(self, token: str) -> RetrieveCheckoutCardVerifyResponse:
        path = "/payment/v1/checkout-card-verify/{}".format(token)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=RetrieveCheckoutCardVerifyResponse
        )

    def retrieve_checkout_payment(self, token: str) -> PaymentResponse:
        path = "/payment/v1/checkout-payments/{}".format(token)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PaymentResponse
        )

    def expire_checkout_payment(self, token: str) -> None:
        path = "/payment/v1/checkout-payments/{}".format(token)
        headers = self._create_headers(None, path)
        self._http_client.request(
            method="DELETE",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=None
        )

    def create_deposit_payment(self, request: CreateDepositPaymentRequest) -> DepositPaymentResponse:
        path = "/payment/v1/deposits"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=DepositPaymentResponse
        )

    def init_3ds_deposit_payment(self, request: CreateDepositPaymentRequest) -> InitThreeDSPaymentResponse:
        path = "/payment/v1/deposits/3ds-init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=InitThreeDSPaymentResponse
        )

    def complete_3ds_deposit_payment(self, request: CompleteThreeDSPaymentRequest) -> DepositPaymentResponse:
        path = "/payment/v1/deposits/3ds-complete"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=DepositPaymentResponse
        )

    def create_fund_transfer_deposit_payment(self,
                                             request: CreateFundTransferDepositPaymentRequest) -> FundTransferDepositPaymentResponse:
        path = "/payment/v1/deposits/fund-transfer"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=FundTransferDepositPaymentResponse
        )

    def init_apm_deposit_payment(self, request: InitApmDepositPaymentRequest) -> ApmDepositPaymentResponse:
        path = "/payment/v1/deposits/apm-init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=ApmDepositPaymentResponse
        )

    def init_garanti_pay_payment(self, request: InitGarantiPayPaymentRequest) -> InitGarantiPayPaymentResponse:
        path = "/payment/v1/garanti-pay-payments"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=InitGarantiPayPaymentResponse
        )

    def init_apm_payment(self, request: InitApmPaymentRequest) -> ApmPaymentInitResponse:
        path = "/payment/v1/apm-payments/init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=ApmPaymentInitResponse
        )

    def complete_apm_payment(self, request: CompleteApmPaymentRequest) -> ApmPaymentCompleteResponse:
        path = "/payment/v1/apm-payments/complete"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=ApmPaymentCompleteResponse
        )

    def create_apm_payment(self, request: CreateApmPaymentRequest) -> PaymentResponse:
        path = "/payment/v1/apm-payments"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentResponse
        )

    def init_pos_apm_payment(self, request: InitPosApmPaymentRequest) -> InitPosApmPaymentResponse:
        path = "/payment/v1/pos-apm-payments/init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=InitPosApmPaymentResponse
        )

    def complete_pos_apm_payment(self, request: CompletePosApmPaymentRequest) -> PaymentResponse:
        path = "/payment/v1/pos-apm-payments/complete"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentResponse
        )

    def retrieve_loyalties(self, request: RetrieveLoyaltiesRequest) -> RetrieveLoyaltiesResponse:
        path = "/payment/v1/card-loyalties/retrieve"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=RetrieveLoyaltiesResponse
        )

    def refund_payment_transaction(self, request: RefundPaymentTransactionRequest) -> PaymentTransactionRefundResponse:
        path = "/payment/v1/refund-transactions"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentTransactionRefundResponse
        )

    def retrieve_payment_transaction_refund(self, refund_transaction_id: int) -> PaymentTransactionRefundResponse:
        path = "/payment/v1/refund-transactions/{}".format(refund_transaction_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PaymentTransactionRefundResponse
        )

    def refund_payment_transaction_mark_as_refunded(
            self, request: RefundPaymentTransactionMarkAsRefundedRequest
    ) -> PaymentTransactionRefundResponse:
        path = "/payment/v1/refund-transactions/mark-as-refunded"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentTransactionRefundResponse
        )

    def refund_payment_mark_as_refunded(
            self, request: RefundPaymentRequest
    ) -> PaymentTransactionRefundListResponse:
        path = "/payment/v1/refunds/mark-as-refunded"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentTransactionRefundListResponse
        )

    def refund_payment(
            self, request: RefundPaymentRequest
    ) -> PaymentRefundResponse:
        path = "/payment/v1/refunds"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentRefundResponse
        )

    def retrieve_payment_refund(self, refund_id: int) -> PaymentRefundResponse:
        path = "/payment/v1/refunds/{}".format(refund_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PaymentRefundResponse
        )

    def store_card(self, request: StoreCardRequest) -> StoredCardResponse:
        path = "/payment/v1/cards"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=StoredCardResponse
        )

    def update_card(self, request: UpdateCardRequest) -> StoredCardResponse:
        path = "/payment/v1/cards/update"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=StoredCardResponse
        )

    def clone_card(self, request: CloneCardRequest) -> StoredCardResponse:
        path = "/payment/v1/cards/clone"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=StoredCardResponse
        )

    def search_stored_cards(self, request: SearchStoredCardsRequest) -> StoredCardListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/payment/v1/cards" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=StoredCardListResponse
        )

    def delete_stored_card(self, request: DeleteStoredCardRequest) -> None:
        path = "/payment/v1/cards/delete"
        headers = self._create_headers(request, path)
        self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=None
        )

    def verify_card(self, request: VerifyCardRequest) -> VerifyCardResponse:
        path = "/payment/v1/cards/verify"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=VerifyCardResponse
        )

    def approve_payment_transactions(self,
                                     request: ApprovePaymentTransactionsRequest) -> PaymentTransactionApprovalListResponse:
        path = "/payment/v1/payment-transactions/approve"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentTransactionApprovalListResponse
        )

    def disapprove_payment_transactions(self,
                                        request: DisapprovePaymentTransactionsRequest) -> PaymentTransactionApprovalListResponse:
        path = "/payment/v1/payment-transactions/disapprove"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentTransactionApprovalListResponse
        )

    def update_payment_transaction(self, request: UpdatePaymentTransactionRequest) -> PaymentTransactionResponse:
        path = "/payment/v1/payment-transactions/{}".format(request.payment_transaction_id)
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="PUT",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentTransactionResponse
        )

    def create_apple_pay_merchant_session(self, request: ApplePayMerchantSessionCreateRequest) -> object:
        path = "/payment/v1/apple-pay/merchant-sessions"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=object
        )

    def retrieve_bnpl_payment_offers(self, request: BnplPaymentOfferRequest) -> BnplPaymentOfferResponse:
        path = "/payment/v1/bnpl-payments/offers"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=BnplPaymentOfferResponse
        )

    def init_bnpl_payment(self, request: InitBnplPaymentRequest) -> InitBnplPaymentResponse:
        path = "/payment/v1/bnpl-payments/init"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=InitBnplPaymentResponse
        )

    def approve_bnpl_payment(self, payment_id: int) -> PaymentResponse:
        path = "/payment/v1/bnpl-payments/{}/approve".format(payment_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=PaymentResponse
        )

    def verify_bnpl_payment(self, payment_id: int) -> BnplPaymentVerifyResponse:
        path = "/payment/v1/bnpl-payments/{}/verify".format(payment_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=BnplPaymentVerifyResponse
        )

    def retrieve_active_banks(self) -> InstantTransferBanksResponse:
        path = "/payment/v1/instant-transfer-banks"
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=InstantTransferBanksResponse
        )

    def retrieve_multi_payment(self, token: str) -> MultiPaymentResponse:
        path = "/payment/v1/multi-payments/{}".format(token)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=MultiPaymentResponse
        )

    def retrieve_provider_cards(self, request: RetrieveProviderCardRequest) -> StoredCardListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/payment/v1/cards/provider-card-mappings{}".format(query)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=StoredCardListResponse
        )

    def is_3d_secure_callback_verified(self, three_d_secure_callback_key: str, params: dict) -> bool:
        hash_val = params.get("hash")
        hash_string = "{}###{}###{}###{}###{}###{}###{}".format(
            three_d_secure_callback_key,
            params.get("status", ""),
            params.get("completeStatus", ""),
            params.get("paymentId", ""),
            params.get("conversationData", ""),
            params.get("conversationId", ""),
            params.get("callbackStatus", "")
        )
        hashed_params = HashGenerator.generate_hash_from_string(hash_string)
        return hash_val == hashed_params
