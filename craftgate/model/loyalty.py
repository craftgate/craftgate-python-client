from typing import Optional

from craftgate.model.loyalty_type import LoyaltyType
from craftgate.model.reward import Reward
from craftgate.model.loyalty_params import LoyaltyParams
from craftgate.model.loyalty_data import LoyaltyData


class Loyalty:
    def __init__(
        self,
        type: Optional[LoyaltyType] = None,
        reward: Optional[Reward] = None,
        message: Optional[str] = None,
        loyalty_params: Optional[LoyaltyParams] = None,
        loyalty_data: Optional[LoyaltyData] = None
    ) -> None:
        self.type = type
        self.reward = reward
        self.message = message
        self.loyalty_params = loyalty_params
        self.loyalty_data = loyalty_data
