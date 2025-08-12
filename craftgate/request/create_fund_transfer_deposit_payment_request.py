from typing import Optional


class CreateFundTransferDepositPaymentRequest(object):
    def __init__(self,
                 price=None,  # type: Optional[float]
                 buyer_member_id=None,  # type: Optional[int]
                 conversation_id=None,  # type: Optional[str]
                 client_ip=None  # type: Optional[str]
                 ):
        self.price = price
        self.buyer_member_id = buyer_member_id
        self.conversation_id = conversation_id
        self.client_ip = client_ip
