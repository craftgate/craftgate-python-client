from typing import Optional
from craftgate.model.settlement_result_status import SettlementResultStatus


class SettlementResponse(object):
    def __init__(
        self,
        settlement_result_status=None  # type: Optional[SettlementResultStatus]
    ):
        self.settlement_result_status = settlement_result_status
