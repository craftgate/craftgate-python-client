from typing import Optional

from craftgate.request.common.base_request import BaseRequest


class RetrieveCardFromIvrRequest(BaseRequest):
    def __init__(
            self,
            card_user_key: Optional[str] = None,
            call_token: Optional[str] = None,
    ) -> None:
        self.card_user_key = card_user_key
        self.call_token = call_token
