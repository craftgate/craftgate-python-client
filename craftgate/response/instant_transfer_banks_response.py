from typing import Optional, List
from craftgate.response.instant_transfer_bank import InstantTransferBank

class InstantTransferBanksResponse(object):
    def __init__(self, items=None):  # type: (Optional[List[InstantTransferBank]]) -> None
        self.items = items or []