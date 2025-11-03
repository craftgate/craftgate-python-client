import json
from datetime import date, datetime
from decimal import Decimal

try:
    from enum import Enum
except ImportError:
    Enum = object


def _to_camel(s):
    if not isinstance(s, str):
        return s
    parts = s.split('_')
    if len(parts) == 1:
        return s
    return parts[0] + ''.join(p[:1].upper() + p[1:] for p in parts[1:])


def _convert(obj):
    try:
        if isinstance(obj, Enum):
            if hasattr(obj, "value") and obj.value is not None:
                return obj.value
            return obj.name
    except Exception:
        pass

    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%dT%H:%M:%S")
    if isinstance(obj, date):
        return obj.strftime("%Y-%m-%d")

    if isinstance(obj, Decimal):
        return float(obj)

    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if v is None:
                continue
            out[_to_camel(k)] = _convert(v)
        return out

    if isinstance(obj, (list, tuple, set)):
        if isinstance(obj, set):
            try:
                seq = sorted(obj)
            except Exception:
                seq = list(obj)
        else:
            seq = obj
        return [_convert(v) for v in seq if v is not None]

    if hasattr(obj, "to_dict") and callable(getattr(obj, "to_dict")):
        return _convert(obj.to_dict())
    if hasattr(obj, "__dict__"):
        d = dict((k, v) for k, v in obj.__dict__.items()
                 if not k.startswith('_') and v is not None)
        return _convert(d)

    return obj


def serialize_request_body(obj):
    cleaned = _convert(obj)
    return json.dumps(
        cleaned,
        ensure_ascii=False,
        separators=(',', ':'),
        sort_keys=True
    )
