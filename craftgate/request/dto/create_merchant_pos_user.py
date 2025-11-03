from typing import Optional

from craftgate.model.pos_operation_type import PosOperationType
from craftgate.model.pos_user_type import PosUserType


class CreateMerchantPosUser(object):
    def __init__(
            self,
            pos_username: Optional[str] = None,
            pos_password: Optional[str] = None,
            pos_user_type: Optional[PosUserType] = None,
            pos_operation_type: Optional[PosOperationType] = None
    ) -> None:
        self.pos_username = pos_username
        self.pos_password = pos_password
        self.pos_user_type = pos_user_type
        self.pos_operation_type = pos_operation_type
