import re
from datetime import datetime
from decimal import Decimal
from typing import get_type_hints, Union, List, Dict

try:
    from enum import Enum
except ImportError:
    Enum = object


class Converter:
    @staticmethod
    def to_clean_dict(obj):
        if obj is None or isinstance(obj, (str, int, float, bool)):
            return obj
        if isinstance(obj, list):
            return [Converter.to_clean_dict(x) for x in obj]
        if isinstance(obj, dict):
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
        try:
            from typing import get_origin, get_args
        except ImportError:
            return t
        origin = getattr(t, "__origin__", None)
        if origin is Union:
            args = [a for a in t.__args__ if a is not type(None)]
            if len(args) == 1:
                return args[0]
        return t

    @staticmethod
    def coerce_value(value, target_type):
        if value is None or target_type is None:
            return value

        target_type = Converter.strip_optional(target_type)

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
            try:
                return datetime.fromisoformat(value.replace('Z', '+00:00'))
            except Exception:
                for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S"):
                    try:
                        return datetime.strptime(value, fmt)
                    except Exception:
                        pass
                return None

        if isinstance(value, dict) and isinstance(target_type, type):
            try:
                return Converter.auto_map(target_type, value)
            except Exception:
                return value

        try:
            from typing import get_origin, get_args
            origin = get_origin(target_type)
            if origin in (list, List):
                (elem_type,) = get_args(target_type)
                return [Converter.coerce_value(v, elem_type) for v in (value or [])]
            if origin in (dict, Dict):
                k_t, v_t = get_args(target_type)
                return {Converter.coerce_value(k, k_t): Converter.coerce_value(v, v_t)
                        for k, v in (value or {}).items()}
        except Exception:
            pass

        return value

    @staticmethod
    def auto_map(cls, data: dict):
        if not data:
            return cls()
        obj = cls()
        hints = {}
        try:
            hints = get_type_hints(cls.__init__)
        except Exception:
            pass

        for key, value in data.items():
            attr_name = Converter.camel_to_snake(key)
            if hasattr(obj, attr_name):
                target_type = hints.get(attr_name)
                coerced = Converter.coerce_value(value, target_type)
                setattr(obj, attr_name, coerced)
        return obj
