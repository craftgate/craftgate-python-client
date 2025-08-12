from typing import Optional
from craftgate.model.pos_user_type import PosUserType
from craftgate.model.pos_operation_type import PosOperationType

class MerchantPosUser(object):
    def __init__(
        self,
        id=None,                   # type: Optional[int]
        pos_username=None,        # type: Optional[str]
        pos_password=None,        # type: Optional[str]
        pos_user_type=None,       # type: Optional[PosUserType]
        pos_operation_type=None   # type: Optional[PosOperationType]
    ):
        self.id = id
        self.pos_username = pos_username
        self.pos_password = pos_password
        self.pos_user_type = pos_user_type
        self.pos_operation_type = pos_operation_type