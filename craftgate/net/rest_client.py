from typing import Dict, Any, Type, Optional

from craftgate.net.base_http_client import BaseHttpClient


class RestClient:
    _client = BaseHttpClient()

    @classmethod
    def get(cls, url: str, headers: Dict[str, str], response_type: Type) -> Any:
        return cls._client.request("GET", url, headers, None, response_type)

    @classmethod
    def post(cls, url: str, headers: Dict[str, str], body: Optional[Dict[str, Any]], response_type: Type) -> Any:
        return cls._client.request("POST", url, headers, body, response_type)

    @classmethod
    def put(cls, url: str, headers: Dict[str, str], body: Optional[Dict[str, Any]], response_type: Type) -> Any:
        return cls._client.request("PUT", url, headers, body, response_type)

    @classmethod
    def delete(cls, url: str, headers: Dict[str, str], response_type: Type) -> Any:
        return cls._client.request("DELETE", url, headers, None, response_type)
