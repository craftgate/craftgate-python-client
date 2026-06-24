import json
from typing import Any, Dict, Optional, Type

import requests  # type: ignore[import]

from craftgate.exception.api_exception import CraftgateException
from craftgate.response.common.response import Response
from craftgate.utils.converter import Converter
from craftgate.utils.serializer import serialize_request_body


class BaseHttpClient:
    CONNECT_TIMEOUT_SECONDS = 10
    READ_TIMEOUT_SECONDS = 150

    def __init__(self, timeout_seconds: int = READ_TIMEOUT_SECONDS):
        self.session = requests.Session()
        self.timeout = timeout_seconds

    def request(
            self,
            method: str,
            url: str,
            headers: Optional[Dict[str, str]],
            body: Optional[Any],
            response_type: Optional[Type[Any]]
    ) -> Any:
        try:
            response = self._send_request(method, url, headers, body)
            self._ensure_http_success(response, response_type)
            if response_type == bytes:
                return response.content
            if response_type is None:
                return None
            return self._map_json_response(response, response_type)
        except CraftgateException:
            raise
        except Exception as ex:
            raise CraftgateException(cause=ex)

    def _send_request(
            self,
            method: str,
            url: str,
            headers: Optional[Dict[str, str]],
            body: Optional[Any]
    ):
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

        timeout = (
            self.CONNECT_TIMEOUT_SECONDS,
            self.timeout if self.timeout else self.READ_TIMEOUT_SECONDS
        )

        response = self.session.send(
            prepared_request,
            timeout=timeout,
            allow_redirects=False
        )

        return response

    def _ensure_http_success(self, response, response_type: Optional[Type[Any]]) -> None:
        if response.status_code < 400:
            if response_type not in (None, bytes) and not response.content:
                raise CraftgateException("1", "Empty response", CraftgateException.GENERAL_ERROR_GROUP)
            return

        raw_text = response.text
        error_code = None
        error_description = None
        error_group = None
        provider_error = None

        try:
            response_json = json.loads(raw_text) if raw_text else {}
            errors_block = response_json.get("errors") if isinstance(response_json, dict) else None
            if isinstance(errors_block, dict):
                error_code = errors_block.get("errorCode")
                error_description = errors_block.get("errorDescription")
                error_group = errors_block.get("errorGroup")
                
                provider_error_block = errors_block.get("providerError")
                if isinstance(provider_error_block, dict):
                    from craftgate.response.common.provider_error import ProviderError
                    provider_error = ProviderError.from_dict(provider_error_block)
        except Exception:
            pass

        if error_code or error_description or error_group:
            raise CraftgateException(error_code, error_description, error_group, provider_error)

        raise CraftgateException()

    def _map_json_response(self, response, response_type: Type[Any]):
        base_response = self._parse_response(response.content)

        data = base_response.data
        if hasattr(response_type, "from_dict") and callable(response_type.from_dict):
            return response_type.from_dict(data)
        return Converter.auto_map(response_type, data)

    def _parse_response(self, content: bytes) -> Response:
        try:
            raw_text = content.decode("utf-8") if isinstance(content, (bytes, bytearray)) else content
            if raw_text is None or raw_text.strip() in ("", "null"):
                raise CraftgateException("1", "Empty response", CraftgateException.GENERAL_ERROR_GROUP)
            response_json = json.loads(raw_text)
        except Exception as ex:
            raise CraftgateException(cause=ex)

        if not isinstance(response_json, dict):
            raise CraftgateException(cause=ValueError("Unexpected response format"))

        return Response.from_dict(response_json)
