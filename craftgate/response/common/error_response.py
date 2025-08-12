class ErrorResponse(object):
    def __init__(self, error_code=None, error_description=None, error_group=None):
        self.error_code = error_code
        self.error_description = error_description
        self.error_group = error_group

    @classmethod
    def from_dict(cls, data):
        if not data or not isinstance(data, dict):
            return cls()

        return cls(
            error_code=data.get("errorCode") or "UNKNOWN_ERROR",
            error_description=data.get("errorDescription") or "No error description provided.",
            error_group=data.get("errorGroup") or "Unknown"
        )

    def to_dict(self):
        return {
            "errorCode": self.error_code,
            "errorDescription": self.error_description,
            "errorGroup": self.error_group
        }

    def __repr__(self):
        return "ErrorResponse(error_code=%r, error_description=%r, error_group=%r)" % (
            self.error_code, self.error_description, self.error_group)
