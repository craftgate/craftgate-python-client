from typing import Optional
from craftgate.model.apm_additional_action import ApmAdditionalAction


class InitMealVoucherCardTokenizationResponse:
    def __init__(
        self,
        session_id: Optional[str] = None,
        additional_action: Optional[ApmAdditionalAction] = None,
        html_content: Optional[str] = None,
        redirect_url: Optional[str] = None
    ) -> None:
        self.session_id = session_id
        self.additional_action = additional_action
        self.html_content = html_content
        self.redirect_url = redirect_url
