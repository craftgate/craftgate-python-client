import urllib.parse
from datetime import datetime, date
from enum import Enum
from typing import Any


class RequestQueryParamsBuilder:

    @staticmethod
    def build_query_params(request: Any):
        if not request:
            return ""

        params = []
        for attr in dir(request):
            if attr.startswith("_") or callable(getattr(request, attr)):
                continue

            value = getattr(request, attr)
            if value is None:
                continue

            key = RequestQueryParamsBuilder._to_camel(attr)

            encoded_value = urllib.parse.quote(
                RequestQueryParamsBuilder._format_value(value),
                safe=":"
            ).replace("+", "%20")

            params.append(f"{key}={encoded_value}")

        return "?" + "&".join(params) if params else ""

    @staticmethod
    def _to_camel(s: str) -> str:
        if not s or "_" not in s:
            return s
        parts = s.split("_")
        return parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])

    @staticmethod
    def _format_value(value):
        if isinstance(value, Enum):
            v = getattr(value, "value", None)
            return str(v if v is not None else value.name)

        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%dT%H:%M:%S")
        if isinstance(value, date):
            return value.strftime("%Y-%m-%d")

        if isinstance(value, (list, tuple, set)):
            return ",".join(RequestQueryParamsBuilder._format_value(v) for v in value)

        return str(value)
