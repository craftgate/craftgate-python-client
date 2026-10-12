
from typing import Optional

class BkmExpressGenerateTokenRequest:
    def __init__(
        self,
        gsm_number: Optional[str] = None,
        user_id: Optional[str] = None
    ) -> None:
        self.gsm_number = gsm_number
        self.user_id = user_id
