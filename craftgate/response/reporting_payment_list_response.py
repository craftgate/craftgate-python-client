from craftgate.response.common.list_response import ListResponse
from craftgate.response.reporting_payment_response import ReportingPaymentResponse


class ReportingPaymentListResponse(ListResponse[ReportingPaymentResponse]):
    item_type = ReportingPaymentResponse
