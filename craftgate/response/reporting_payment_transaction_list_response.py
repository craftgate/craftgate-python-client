from craftgate.response.common.list_response import ListResponse
from craftgate.response.dto.reporting_payment_transaction import ReportingPaymentTransaction


class ReportingPaymentTransactionListResponse(ListResponse[ReportingPaymentTransaction]):
    item_type = ReportingPaymentTransaction
