from typing import Optional


class MerchantPos:
    def __init__(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        alias: Optional[str] = None,
        bank_id: Optional[int] = None
    ) -> None:
        self.id = id
        self.name = name
        self.alias = alias
        self.bank_id = bank_id
