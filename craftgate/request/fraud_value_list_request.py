class FraudValueListRequest(object):
    def __init__(self,
                 list_name=None,
                 label=None,
                 type=None,
                 value=None,
                 duration_in_seconds=None,
                 payment_id=None):
        self.list_name = list_name
        self.label = label
        self.type = type
        self.value = value
        self.duration_in_seconds = duration_in_seconds
        self.payment_id = payment_id
