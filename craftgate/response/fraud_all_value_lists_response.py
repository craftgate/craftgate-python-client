from craftgate.response.common.list_response import ListResponse
from craftgate.response.fraud_value_list_response import FraudValueListResponse


class FraudAllValueListsResponse(ListResponse[FraudValueListResponse]):
    item_type = FraudValueListResponse
