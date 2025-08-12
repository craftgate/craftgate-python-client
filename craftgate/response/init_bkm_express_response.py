from typing import Optional


class InitBkmExpressResponse:
    def __init__(
        self,
        id: Optional[str] = None,
        path: Optional[str] = None,
        token: Optional[str] = None
    ) -> None:
        self.id = id
        self.path = path
        self.token = token
