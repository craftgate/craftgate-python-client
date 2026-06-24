from typing import Optional


def __init__(
        self,
        token: Optional[str] = None,
        error_message: Optional[str] = None,
        error_code: Optional[str] = None
) -> None:
    self.token = token
    self.error_message = error_message
    self.error_code = error_code


class BkmExpressGenerateTokenResponse:
    pass
