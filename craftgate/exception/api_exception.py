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

        message = raw if (prefer_raw_message and raw) else self.error_description
        super(CraftgateException, self).__init__(message)

    def __str__(self):
        if self.prefer_raw_message and self.raw:
            return self.raw
        return self._format_details()

    def __repr__(self):
        return self._format_details()

    def _format_details(self) -> str:
        return "CraftgateException(errorCode={}, errorDescription={}, errorGroup={})".format(
            self.error_code,
            self.error_description,
            self.error_group
        )
