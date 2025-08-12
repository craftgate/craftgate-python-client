class AutopilotState(object):
    def __init__(self, is_three_ds_up=None, is_non_three_ds_up=None):
        # type: (Optional[bool], Optional[bool]) -> None
        self.is_three_ds_up = is_three_ds_up
        self.is_non_three_ds_up = is_non_three_ds_up