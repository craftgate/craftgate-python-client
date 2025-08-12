from typing import List, Optional

from craftgate.response.dto.installment import Installment


class InstallmentListResponse(object):
    def __init__(self, items=None):
        # type: (Optional[List[Installment]]) -> None
        self.items = items