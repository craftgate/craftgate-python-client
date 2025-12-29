from craftgate.response.common.provider_error import ProviderError

class ErrorResponse(object):
    def __init__(self, error_code=None, error_description=None, error_group=None, provider_error=None):
        self.error_code = error_code
        self.error_description = error_description
        self.error_group = error_group
        self.provider_error = provider_error

    @classmethod
    def from_dict(cls, data):
        if not data or not isinstance(data, dict):
            return cls()

        return cls(
            error_code=data.get("errorCode") or "UNKNOWN_ERROR",
            error_description=data.get("errorDescription") or "No error description provided.",
            error_group=data.get("errorGroup") or "Unknown",
            provider_error=ProviderError.from_dict(data.get("providerError"))
        )

    def to_dict(self):
        result = {
            "errorCode": self.error_code,
            "errorDescription": self.error_description,
            "errorGroup": self.error_group
        }
        if self.provider_error:
            result["providerError"] = self.provider_error.to_dict()
        return result

    def __repr__(self):
        if self.provider_error:
            return "ErrorResponse(error_code=%r, error_description=%r, error_group=%r, provider_error=%r)" % (
                self.error_code, self.error_description, self.error_group, self.provider_error)
        return "ErrorResponse(error_code=%r, error_description=%r, error_group=%r)" % (
            self.error_code, self.error_description, self.error_group)
