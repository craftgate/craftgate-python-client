from typing import Optional


class MasterpassAccountTokenGenerateResponse(object):
    def __init__(
            self,
            token: Optional[str] = None
    ) -> None:
        self.token = token
