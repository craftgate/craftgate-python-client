from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.member_type import MemberType
from craftgate.model.settlement_earnings_destination import SettlementEarningsDestination
from craftgate.model.status import Status


class MemberResponse(object):
    def __init__(
        self,
        id=None,  # type: Optional[int]
        created_date=None,  # type: Optional[datetime]
        updated_date=None,  # type: Optional[datetime]
        status=None,  # type: Optional[Status]
        is_buyer=None,  # type: Optional[bool]
        is_sub_merchant=None,  # type: Optional[bool]
        member_type=None,  # type: Optional[MemberType]
        member_external_id=None,  # type: Optional[str]
        name=None,  # type: Optional[str]
        email=None,  # type: Optional[str]
        address=None,  # type: Optional[str]
        phone_number=None,  # type: Optional[str]
        contact_name=None,  # type: Optional[str]
        contact_surname=None,  # type: Optional[str]
        legal_company_title=None,  # type: Optional[str]
        tax_office=None,  # type: Optional[str]
        tax_number=None,  # type: Optional[str]
        settlement_earnings_destination=None,  # type: Optional[SettlementEarningsDestination]
        negative_wallet_amount_limit=None,  # type: Optional[Decimal]  # Deprecated
        iban=None,  # type: Optional[str]
        settlement_delay_count=None  # type: Optional[int]
    ):
        self.id = id
        self.created_date = created_date
        self.updated_date = updated_date
        self.status = status
        self.is_buyer = is_buyer
        self.is_sub_merchant = is_sub_merchant
        self.member_type = member_type
        self.member_external_id = member_external_id
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.contact_name = contact_name
        self.contact_surname = contact_surname
        self.legal_company_title = legal_company_title
        self.tax_office = tax_office
        self.tax_number = tax_number
        self.settlement_earnings_destination = settlement_earnings_destination
        self.negative_wallet_amount_limit = negative_wallet_amount_limit
        self.iban = iban
        self.settlement_delay_count = settlement_delay_count