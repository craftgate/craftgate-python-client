from typing import List, Optional

from craftgate.response.compay_bank import CompayBank


class CompayBanksResponse(object):
    def __init__(self, items: Optional[List[CompayBank]] = None) -> None:
        self.items = items
