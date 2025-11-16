import base64
import hashlib
import urllib.parse

from craftgate.exception.api_exception import CraftgateException
from craftgate.utils.serializer import serialize_request_body


class HashGenerator:

    @staticmethod
    def generate_hash(base_url, api_key, secret_key, random_string, request, path):
        try:
            base = base_url or ""
            route = path or ""
            decoded_url = urllib.parse.unquote_plus(base + route, encoding="utf-8", errors="strict")
            body_str = ""
            if request is not None:
                body_str = serialize_request_body(request)

            data_to_sign = decoded_url + api_key + secret_key + random_string + body_str

            digest = hashlib.sha256(data_to_sign.encode("utf-8")).digest()
            return base64.b64encode(digest).decode("utf-8")

        except Exception as e:
            raise CraftgateException(cause=e)

    @staticmethod
    def generate_hash_from_string(value: str) -> str:
        try:
            return hashlib.sha256(value.encode("utf-8")).hexdigest()
        except Exception as e:
            raise CraftgateException(cause=e)
