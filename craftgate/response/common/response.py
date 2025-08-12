class Response(object):
    def __init__(self, errors=None, data=None):
        self.errors = errors
        self.data = data

    @classmethod
    def from_dict(cls, raw):
        errors = None
        if raw.get("errors"):
            from craftgate.response.common.error_response import ErrorResponse
            errors = ErrorResponse.from_dict(raw.get("errors"))
        return cls(errors=errors, data=raw.get("data"))

    def to_dict(self):
        return {
            "errors": self.errors.to_dict() if self.errors else None,
            "data": self._serialize_data()
        }

    def _serialize_data(self):
        if hasattr(self.data, "to_dict") and callable(getattr(self.data, "to_dict")):
            return self.data.to_dict()
        return self.data

    def __repr__(self):
        return "Response(errors=%r, data=%r)" % (self.errors, self.data)
