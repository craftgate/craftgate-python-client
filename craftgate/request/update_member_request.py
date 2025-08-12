from typing import Optional
from decimal import Decimal

from craftgate.model.member_type import MemberType
from craftgate.model.settlement_earnings_destination import SettlementEarningsDestination


class UpdateMemberRequest(object):
    def __init__(
            self,
            name: Optional[str] = None,
            address: Optional[str] = None,
            email: Optional[str] = None,
            phone_number: Optional[str] = None,
            contact_name: Optional[str] = None,
            contact_surname: Optional[str] = None,
            member_type: Optional[MemberType] = None,
            legal_company_title: Optional[str] = None,
            tax_office: Optional[str] = None,
            tax_number: Optional[str] = None,
            iban: Optional[str] = None,
            settlement_earnings_destination: Optional[SettlementEarningsDestination] = None,
            negative_wallet_amount_limit: Optional[Decimal] = None, #deprecated
            sub_merchant_maximum_allowed_negative_balance: Optional[Decimal] = None,
            is_buyer: Optional[bool] = None,
            is_sub_merchant: Optional[bool] = None,
            settlement_delay_count: Optional[int] = None
    ) -> None:
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
