from typing import Optional


class HeaderOptions(object):
    """Carries the request-scoped options that travel as headers rather than in the payload.

    A distinct type from ``BaseRequest`` so the header layer cannot reach path variables or body
    fields, and from ``RequestOptions``, which holds client configuration.
    """

    def __init__(self, idempotency_key: Optional[str] = None) -> None:
        self.idempotency_key = idempotency_key
