class CraftgateException(Exception):
    GENERAL_ERROR_CODE = "0"
    GENERAL_ERROR_DESCRIPTION = "An error occurred."
    GENERAL_ERROR_GROUP = "Unknown"

    def __init__(
            self,
            error_code=None,
            error_description=None,
            error_group=None,
            cause=None,
            raw=None,
            prefer_raw_message=False
    ):
        self.error_code = error_code or self.GENERAL_ERROR_CODE
        self.error_description = error_description or self.GENERAL_ERROR_DESCRIPTION
        self.error_group = error_group or self.GENERAL_ERROR_GROUP
        self.cause = cause
        self.raw = raw
        self.prefer_raw_message = prefer_raw_message

        msg = raw if (prefer_raw_message and raw) else "[{}] {}: {}".format(
            self.error_group, self.error_code, self.error_description
        )
        super(CraftgateException, self).__init__(msg)

    def __str__(self):
        if self.prefer_raw_message and self.raw:
            return self.raw
        return "[{}] {}: {}".format(self.error_group, self.error_code, self.error_description)
