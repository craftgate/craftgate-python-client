import json

import requests

from craftgate.exception.api_exception import CraftgateException
from craftgate.response.common.response import Response
from craftgate.utils.converter import Converter
from craftgate.utils.serializer import serialize_request_body


class BaseHttpClient:
    def __init__(self, timeout_seconds=150):
        self.session = requests.Session()
        self.timeout = timeout_seconds

    def request(self, method, url, headers, body, response_type):
        try:
            response = self._send_request(method, url, headers, body)
            if response_type == bytes:
                return response.content
            return self._handle_json_response(response, response_type)
        except CraftgateException:
            raise
        except Exception as ex:
            raise CraftgateException(cause=ex)

    def _send_request(self, method, url, headers, body):
        if headers is None:
            headers = {}

        if not headers.get('Content-Type'):
            headers['Content-Type'] = 'application/json; charset=utf-8'
        if not headers.get('Accept'):
            headers['Accept'] = 'application/json'

        serialized_body = None
        if body is not None:
            serialized_body = serialize_request_body(body)
            serialized_body = serialized_body.encode('utf-8')

        request = requests.Request(
            method=method.upper(),
            url=url,
            headers=headers,
            data=serialized_body
        )
        prepared_request = self.session.prepare_request(request)

        response = self.session.send(
            prepared_request,
            timeout=self.timeout,
            allow_redirects=False
        )

        return response

    def _handle_json_response(self, response, response_type):
        content = response.content

        if response.status_code >= 400:
            raw_text = None
            errors_code = None
            errors_desc = None
            errors_group = None

            try:
                raw_text = response.text
                response_json = json.loads(raw_text) if raw_text else {}
                errors_block = response_json.get("errors") if isinstance(response_json, dict) else None
                if isinstance(errors_block, dict):
                    errors_code = errors_block.get("errorCode")
                    errors_desc = errors_block.get("errorDescription")
                    errors_group = errors_block.get("errorGroup")
            except Exception as parse_ex:
                pass

            raise CraftgateException(
                error_code=errors_code or "UNKNOWN_ERROR",
                error_description=errors_desc or (raw_text or "An error occurred."),
                error_group=errors_group or "Unknown",
                raw=raw_text,
                prefer_raw_message=True
            )

        if response_type is not None and content in (None, b"", b"null"):
            raise CraftgateException("1", "Empty response", "Unknown")

        if content in (None, b"", b"null"):
            return None

        try:
            raw_text = response.text
            response_json = json.loads(raw_text)
        except Exception:
            return None

        base_response = Response.from_dict(response_json)
        if base_response and base_response.errors:
            raise CraftgateException(
                error_code=getattr(base_response.errors, "error_code", None),
                error_description=getattr(base_response.errors, "error_description", None),
                error_group=getattr(base_response.errors, "error_group", None)
            )

        if response_type is None:
            return None

        data = base_response.data if base_response else None
        if hasattr(response_type, "from_dict") and callable(response_type.from_dict):
            return response_type.from_dict(data)
        else:
            return Converter.auto_map(response_type, data)
