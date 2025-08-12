import re
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Any, Dict, List, Set, Union, get_type_hints

try:
    from typing import get_origin as _get_origin, get_args as _get_args  # type: ignore[attr-defined]
except ImportError:
    def _get_origin(tp):
        return getattr(tp, "__origin__", None)


    def _get_args(tp):
        return getattr(tp, "__args__", ())

from craftgate.utils.attribute_dict import AttributeDict


class Converter:
    _patched_serializable_classes: Set[type] = set()

    @staticmethod
    def to_clean_dict(obj):
        try:
            if isinstance(obj, Enum):
                if hasattr(obj, "value") and obj.value is not None:
                    return obj.value
                return obj.name
        except Exception:
            pass
        if obj is None or isinstance(obj, (str, int, float, bool)):
            return obj
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, list):
            return [Converter.to_clean_dict(x) for x in obj]
        if isinstance(obj, dict):
            return {k: Converter.to_clean_dict(v) for k, v in obj.items() if v is not None}
        if isinstance(obj, AttributeDict):
            return {k: Converter.to_clean_dict(v) for k, v in obj.items() if v is not None}

        try:
            return {
                k: Converter.to_clean_dict(v)
                for k, v in vars(obj).items()
                if not k.startswith('_') and v is not None
            }
        except Exception:
            return obj

    @staticmethod
    def camel_to_snake(name: str) -> str:
        s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    @staticmethod
    def strip_optional(t):
        origin = _get_origin(t)
        if origin is Union or str(origin) == "typing.Union":
            args = [a for a in _get_args(t) if a is not type(None)]
            if len(args) == 1:
                return args[0]
        return t

    @staticmethod
    def _ensure_serializable(target_type):
        if not isinstance(target_type, type):
            return
        if target_type in Converter._patched_serializable_classes:
            return
        if issubclass(target_type, (str, int, float, bool, Decimal, datetime)):
            return
        try:
            if issubclass(target_type, Enum):
                return
        except Exception:
            pass
        if target_type.__module__ == 'typing':
            return

        if not hasattr(target_type, "to_dict"):
            def to_dict(self):
                return Converter.to_clean_dict(self)

            setattr(target_type, "to_dict", to_dict)

        if "__repr__" not in target_type.__dict__:
            def __repr__(self):
                return "{}({})".format(self.__class__.__name__, Converter.to_clean_dict(self))

            setattr(target_type, "__repr__", __repr__)

        if "__iter__" not in target_type.__dict__:
            def __iter__(self):
                for key, value in Converter.to_clean_dict(self).items():
                    yield key, value

            setattr(target_type, "__iter__", __iter__)

        Converter._patched_serializable_classes.add(target_type)

    @staticmethod
    def coerce_value(value, target_type):
        if value is None:
            return value

        if target_type is None:
            return Converter._coerce_untyped(value)

        target_type = Converter.strip_optional(target_type)
        if target_type is Any:
            return Converter._coerce_untyped(value)
        Converter._ensure_serializable(target_type)

        try:
            if isinstance(target_type, type) and issubclass(target_type, Enum):
                if isinstance(value, target_type):
                    return value
                return target_type(value)
        except Exception:
            pass

        if target_type is Decimal and not isinstance(value, Decimal):
            return Decimal(str(value))

        if target_type is datetime and isinstance(value, str):
            normalized_value = value.replace('Z', '+00:00')
            if hasattr(datetime, "fromisoformat"):
                try:
                    parsed = datetime.fromisoformat(normalized_value)
                    if parsed.tzinfo is not None:
                        parsed = parsed.replace(tzinfo=None)
                    return parsed
                except Exception:
                    pass
            formats = (
                "%Y-%m-%dT%H:%M:%S.%f%z",
                "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%dT%H:%M:%S.%f",
                "%Y-%m-%dT%H:%M:%S"
            )
            for fmt in formats:
                try:
                    candidate = normalized_value
                    if "%z" in fmt and len(candidate) >= 6 and candidate[-3] == ":" and candidate[-6] in "+-":
                        candidate = candidate[:-3] + candidate[-2:]
                    parsed = datetime.strptime(candidate, fmt)
                    if parsed.tzinfo is not None:
                        parsed = parsed.replace(tzinfo=None)
                    return parsed
                except Exception:
                    continue
            return None

        if isinstance(value, dict) and isinstance(target_type, type):
            try:
                return Converter.auto_map(target_type, value)
            except Exception:
                return Converter._coerce_untyped(value)

        origin = _get_origin(target_type)
        args = _get_args(target_type)
        if origin in (list, List) or str(origin) in ("typing.List", "list"):
            elem_type = args[0] if args else None
            return [Converter.coerce_value(v, elem_type) for v in (value or [])]
        if origin in (dict, Dict) or str(origin) in ("typing.Dict", "dict"):
            key_type = args[0] if len(args) > 0 else None
            value_type = args[1] if len(args) > 1 else None
            return {
                Converter.coerce_value(k, key_type): Converter.coerce_value(v, value_type)
                for k, v in (value or {}).items()
            }

        return value

    @staticmethod
    def auto_map(cls, data: dict):
        if not data:
            return cls()
        Converter._ensure_serializable(cls)
        obj = cls()
        hints = {}
        for current in reversed(cls.__mro__):
            init = getattr(current, "__init__", None)
            if not init:
                continue
            try:
                current_hints = get_type_hints(init)
            except Exception:
                current_hints = {}
            for key, value in current_hints.items():
                if key == "return":
                    continue
                if key not in hints:
                    hints[key] = value

        for key, value in data.items():
            attr_name = Converter.camel_to_snake(key)
            target_type = hints.get(attr_name)
            coerced = Converter.coerce_value(value, target_type)
            setattr(obj, attr_name, coerced)
        return obj

    @staticmethod
    def _coerce_untyped(value):
        if isinstance(value, AttributeDict):
            return value
        if isinstance(value, dict):
            return AttributeDict(value)
        if isinstance(value, list):
            return [Converter._coerce_untyped(v) for v in value]
        if isinstance(value, tuple):
            return tuple(Converter._coerce_untyped(v) for v in value)
        return value
