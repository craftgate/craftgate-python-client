from decimal import Decimal
from typing import Optional


class Reward:
    def __init__(
            self,
            card_reward_money: Optional[Decimal] = None,
            firm_reward_money: Optional[Decimal] = None,
            total_reward_money: Optional[Decimal] = None
    ) -> None:
        self.card_reward_money = card_reward_money
        self.firm_reward_money = firm_reward_money
        self.total_reward_money = total_reward_money
