import urllib.parse
from datetime import date, datetime
from enum import Enum
from typing import Any, Iterable, Mapping, Tuple


class RequestQueryParamsBuilder:

    @staticmethod
    def build_query_params(request: Any) -> str:
        if request is None:
            return ""

        params = []
        for attr, value in RequestQueryParamsBuilder._iterate_fields(request):
            if value is None:
                continue

            key = RequestQueryParamsBuilder._to_camel(attr)

            encoded_value = urllib.parse.quote(
                RequestQueryParamsBuilder._format_value(value),
                safe=""
            ).replace("+", "%20")

            params.append(f"{key}={encoded_value}")

        return "?" + "&".join(params) if params else ""

    @staticmethod
    def _iterate_fields(request: Any) -> Iterable[Tuple[str, Any]]:
        if isinstance(request, Mapping):
            return ((key, value) for key, value in request.items() if not str(key).startswith("_"))

        if hasattr(request, "__dict__"):
            return (
                (attr, value)
                for attr, value in request.__dict__.items()
                if not attr.startswith("_")
            )

        fields = []
        for attr in dir(request):
            if attr.startswith("_"):
                continue
            value = getattr(request, attr)
            if callable(value):
                continue
            fields.append((attr, value))
        return fields

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

        if isinstance(value, bool):
            return "true" if value else "false"

        if isinstance(value, datetime):
            return RequestQueryParamsBuilder._format_datetime(value)
        if isinstance(value, date):
            return value.strftime("%Y-%m-%d")

        if isinstance(value, (list, tuple, set)):
            return ",".join(RequestQueryParamsBuilder._format_value(v) for v in value)

        return str(value)

    @staticmethod
    def _format_datetime(value: datetime) -> str:
        naive_value = value.replace(tzinfo=None) if getattr(value, "tzinfo", None) else value
        base = naive_value.strftime("%Y-%m-%dT%H:%M:%S")
        if naive_value.microsecond:
            fractional = f"{naive_value.microsecond:06d}".rstrip("0")
            return f"{base}.{fractional}"
        return base
