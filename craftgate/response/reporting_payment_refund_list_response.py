from craftgate.response.common.list_response import ListResponse
from craftgate.response.reporting_payment_refund_response import ReportingPaymentRefundResponse


class ReportingPaymentRefundListResponse(ListResponse[ReportingPaymentRefundResponse]):
    item_type = ReportingPaymentRefundResponse
