from typing import List, Optional

from craftgate.response.dto.installment import Installment


class InstallmentListResponse(object):
    def __init__(self, items: Optional[List[Installment]] = None) -> None:
        self.items = items
