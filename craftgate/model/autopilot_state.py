from typing import Optional


class AutopilotState(object):
    def __init__(
            self,
            is_three_ds_up: Optional[bool] = None,
            is_non_three_ds_up: Optional[bool] = None
    ) -> None:
        self.is_three_ds_up = is_three_ds_up
        self.is_non_three_ds_up = is_non_three_ds_up
