from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.approve_payment_transactions_request import ApprovePaymentTransactionsRequest
from craftgate.request.create_instant_wallet_settlement_request import CreateInstantWalletSettlementRequest
from craftgate.request.disapprove_payment_transactions_request import DisapprovePaymentTransactionsRequest
from craftgate.request.update_payment_transaction_request import UpdatePaymentTransactionRequest
from craftgate.request_options import RequestOptions
from craftgate.response.payment_transaction_approval_list_response import PaymentTransactionApprovalListResponse
from craftgate.response.payment_tx_payout_response import PaymentTxPayoutResponse
from craftgate.response.settlement_response import SettlementResponse


class SettlementAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(SettlementAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def create_instant_wallet_settlement(self, request: CreateInstantWalletSettlementRequest) -> SettlementResponse:
        path = "/settlement/v1/instant-wallet-settlements"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=SettlementResponse
        )

    def approve_payment_transactions(self,
                                     request: ApprovePaymentTransactionsRequest) -> PaymentTransactionApprovalListResponse:
        path = "/settlement/v1/payment-transactions/approve"
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
        path = "/settlement/v1/payment-transactions/disapprove"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentTransactionApprovalListResponse
        )

    def update_payment_transaction(self, request: UpdatePaymentTransactionRequest) -> PaymentTxPayoutResponse:
        path = "/settlement/v1/payment-transactions/{}".format(request.payment_transaction_id)
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="PUT",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=PaymentTxPayoutResponse
        )
