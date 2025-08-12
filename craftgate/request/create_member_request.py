from decimal import Decimal
from typing import Optional

from craftgate.model.member_type import MemberType
from craftgate.model.settlement_earnings_destination import SettlementEarningsDestination


class CreateMemberRequest(object):
    def __init__(
            self,
            member_external_id=None,  # type: Optional[str]
            name=None,  # type: Optional[str]
            address=None,  # type: Optional[str]
            email=None,  # type: Optional[str]
            phone_number=None,  # type: Optional[str]
            contact_name=None,  # type: Optional[str]
            contact_surname=None,  # type: Optional[str]
            member_type=None,  # type: Optional[MemberType]
            legal_company_title=None,  # type: Optional[str]
            tax_office=None,  # type: Optional[str]
            tax_number=None,  # type: Optional[str]
            iban=None,  # type: Optional[str]
            settlement_earnings_destination=None,  # type: Optional[SettlementEarningsDestination]
            negative_wallet_amount_limit=None,  # type: Optional[Decimal]  # Deprecated
            sub_merchant_maximum_allowed_negative_balance=None,  # type: Optional[Decimal]
            is_buyer=None,  # type: Optional[bool]
            is_sub_merchant=None,  # type: Optional[bool]
            settlement_delay_count=None  # type: Optional[int]
    ):
        self.member_external_id = member_external_id
        self.name = name
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.contact_name = contact_name
        self.contact_surname = contact_surname
        self.member_type = member_type
        self.legal_company_title = legal_company_title
        self.tax_office = tax_office
        self.tax_number = tax_number
        self.iban = iban
        self.settlement_earnings_destination = settlement_earnings_destination
        self.negative_wallet_amount_limit = negative_wallet_amount_limit  # Deprecated
        self.sub_merchant_maximum_allowed_negative_balance = sub_merchant_maximum_allowed_negative_balance
        self.is_buyer = is_buyer
        self.is_sub_merchant = is_sub_merchant
        self.settlement_delay_count = settlement_delay_count
