from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class DeleteValueListRequest(BaseRequest):
    def __init__(
            self,
            list_name: Optional[str] = None
    ) -> None:
        self.list_name = list_name
