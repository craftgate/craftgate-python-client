from craftgate.adapter.base_adapter import BaseAdapter
from craftgate.net.base_http_client import BaseHttpClient
from craftgate.request.create_remittance_request import CreateRemittanceRequest
from craftgate.request.create_wallet_request import CreateWalletRequest
from craftgate.request.create_withdraw_request import CreateWithdrawRequest
from craftgate.request.refund_wallet_transaction_to_card_request import RefundWalletTransactionToCardRequest
from craftgate.request.reset_merchant_member_wallet_balance_request import ResetMerchantMemberWalletBalanceRequest
from craftgate.request.search_wallet_transactions_request import SearchWalletTransactionsRequest
from craftgate.request.search_withdraws_request import SearchWithdrawsRequest
from craftgate.request.update_wallet_request import UpdateWalletRequest
from craftgate.request_options import RequestOptions
from craftgate.response.refund_wallet_transaction_list_response import RefundWalletTransactionListResponse
from craftgate.response.refund_wallet_transaction_response import RefundWalletTransactionResponse
from craftgate.response.remittance_response import RemittanceResponse
from craftgate.response.wallet_response import WalletResponse
from craftgate.response.wallet_transaction_list_response import WalletTransactionListResponse
from craftgate.response.wallet_transaction_refundable_amount_response import WalletTransactionRefundableAmountResponse
from craftgate.response.withdraw_list_response import WithdrawListResponse
from craftgate.response.withdraw_response import WithdrawResponse
from craftgate.utils.request_query_params_builder import RequestQueryParamsBuilder


class WalletAdapter(BaseAdapter):
    def __init__(self, request_options: RequestOptions) -> None:
        super(WalletAdapter, self).__init__(request_options)
        self._http_client = BaseHttpClient()

    def create_wallet(self, member_id: int, request: CreateWalletRequest) -> WalletResponse:
        path = "/wallet/v1/members/{}/wallets".format(member_id)
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=WalletResponse
        )

    def retrieve_member_wallet(self, member_id: int) -> WalletResponse:
        path = "/wallet/v1/members/{}/wallet".format(member_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=WalletResponse
        )

    def search_wallet_transactions(
            self, wallet_id: int, request: SearchWalletTransactionsRequest
    ) -> WalletTransactionListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/wallet/v1/wallets/{}/wallet-transactions{}".format(wallet_id, query)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=WalletTransactionListResponse
        )

    def update_wallet(self, member_id: int, wallet_id: int, request: UpdateWalletRequest) -> WalletResponse:
        path = "/wallet/v1/members/{}/wallets/{}".format(member_id, wallet_id)
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="PUT",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=WalletResponse
        )

    def send_remittance(self, request: CreateRemittanceRequest) -> RemittanceResponse:
        path = "/wallet/v1/remittances/send"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=RemittanceResponse
        )

    def receive_remittance(self, request: CreateRemittanceRequest) -> RemittanceResponse:
        path = "/wallet/v1/remittances/receive"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=RemittanceResponse
        )

    def retrieve_remittance(self, remittance_id: int) -> RemittanceResponse:
        path = "/wallet/v1/remittances/{}".format(remittance_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=RemittanceResponse
        )

    def retrieve_merchant_member_wallet(self) -> WalletResponse:
        path = "/wallet/v1/merchants/me/wallet"
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=WalletResponse
        )

    def reset_merchant_member_wallet_balance(
            self, request: ResetMerchantMemberWalletBalanceRequest
    ) -> WalletResponse:
        path = "/wallet/v1/merchants/me/wallet/reset-balance"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=WalletResponse
        )

    def retrieve_refundable_amount_of_wallet_transaction(
            self, wallet_transaction_id: int
    ) -> WalletTransactionRefundableAmountResponse:
        path = "/payment/v1/wallet-transactions/{}/refundable-amount".format(wallet_transaction_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=WalletTransactionRefundableAmountResponse
        )

    def refund_wallet_transaction(
            self, wallet_transaction_id: int, request: RefundWalletTransactionToCardRequest
    ) -> RefundWalletTransactionResponse:
        path = "/payment/v1/wallet-transactions/{}/refunds".format(wallet_transaction_id)
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=RefundWalletTransactionResponse
        )

    def retrieve_refund_wallet_transactions(
            self, wallet_transaction_id: int
    ) -> RefundWalletTransactionListResponse:
        path = "/payment/v1/wallet-transactions/{}/refunds".format(wallet_transaction_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=RefundWalletTransactionListResponse
        )

    def create_withdraw(self, request: CreateWithdrawRequest) -> WithdrawResponse:
        path = "/wallet/v1/withdraws"
        headers = self._create_headers(request, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=request,
            response_type=WithdrawResponse
        )

    def cancel_withdraw(self, withdraw_id: int) -> WithdrawResponse:
        path = "/wallet/v1/withdraws/{}/cancel".format(withdraw_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="POST",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=WithdrawResponse
        )

    def retrieve_withdraw(self, withdraw_id: int) -> WithdrawResponse:
        path = "/wallet/v1/withdraws/{}".format(withdraw_id)
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=WithdrawResponse
        )

    def search_withdraws(self, request: SearchWithdrawsRequest) -> WithdrawListResponse:
        query = RequestQueryParamsBuilder.build_query_params(request)
        path = "/wallet/v1/withdraws" + query
        headers = self._create_headers(None, path)
        return self._http_client.request(
            method="GET",
            url=self.request_options.base_url + path,
            headers=headers,
            body=None,
            response_type=WithdrawListResponse
        )
