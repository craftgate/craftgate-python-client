from craftgate.response.common.list_response import ListResponse
from craftgate.response.dto.fraud_check import FraudCheck


class FraudCheckListResponse(ListResponse[FraudCheck]):
    item_type = FraudCheck
