from datetime import datetime
from decimal import Decimal
from typing import Optional

from craftgate.model.member_type import MemberType
from craftgate.model.settlement_earnings_destination import SettlementEarningsDestination
from craftgate.model.status import Status


class MemberResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            created_date: Optional[datetime] = None,
            updated_date: Optional[datetime] = None,
            status: Optional[Status] = None,
            is_buyer: Optional[bool] = None,
            is_sub_merchant: Optional[bool] = None,
            member_type: Optional[MemberType] = None,
            member_external_id: Optional[str] = None,
            name: Optional[str] = None,
            email: Optional[str] = None,
            address: Optional[str] = None,
            phone_number: Optional[str] = None,
            contact_name: Optional[str] = None,
            contact_surname: Optional[str] = None,
            legal_company_title: Optional[str] = None,
            tax_office: Optional[str] = None,
            tax_number: Optional[str] = None,
            settlement_earnings_destination: Optional[SettlementEarningsDestination] = None,
            negative_wallet_amount_limit: Optional[Decimal] = None,
            iban: Optional[str] = None,
            settlement_delay_count: Optional[int] = None
    ) -> None:
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
