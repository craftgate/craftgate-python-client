from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class RemoveValueFromValueListRequest(BaseRequest):
    def __init__(
            self,
            list_name: Optional[str] = None,
            value_id: Optional[str] = None
    ) -> None:
        self.list_name = list_name
        self.value_id = value_id
