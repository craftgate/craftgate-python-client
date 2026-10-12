from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class DeleteProductRequest(BaseRequest):
    def __init__(
            self,
            id: Optional[int] = None
    ) -> None:
        self.id = id
