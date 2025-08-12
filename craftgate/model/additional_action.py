from enum import Enum

class AdditionalAction(str, Enum):
    REDIRECT_TO_URL = "REDIRECT_TO_URL"
    CONTINUE_IN_CLIENT = "CONTINUE_IN_CLIENT"
    SHOW_HTML_CONTENT = "SHOW_HTML_CONTENT"
    NONE = "NONE"