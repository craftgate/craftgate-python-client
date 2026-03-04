class ProviderError(object):
    def __init__(self, error_code=None, error_message=None):
        self.error_code = error_code
        self.error_message = error_message

    @classmethod
    def from_dict(cls, data):
        if not data or not isinstance(data, dict):
            return None

        return cls(
            error_code=data.get("errorCode"),
            error_message=data.get("errorMessage")
        )

    def to_dict(self):
        return {
            "errorCode": self.error_code,
            "errorMessage": self.error_message
        }

    def __repr__(self):
        return "ProviderError(error_code=%r, error_message=%r)" % (
            self.error_code, self.error_message)
