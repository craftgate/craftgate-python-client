from craftgate.response.common.list_response import ListResponse
from craftgate.response.dto.fraud_rule import FraudRule

class FraudRuleResponse(ListResponse[FraudRule]):
    item_type = FraudRule
