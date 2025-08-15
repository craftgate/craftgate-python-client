# tests/test_onboarding_sample.py
import os
import unittest
import uuid

from craftgate import Craftgate, RequestOptions
from craftgate.model import MemberType, SettlementEarningsDestination
from craftgate.request import CreateMemberRequest, CreateMerchantRequest, SearchMembersRequest, UpdateMemberRequest


class OnboardingSample(unittest.TestCase):
    API_KEY = os.environ.get("CG_API_KEY", "YOUR_API_KEY")
    SECRET_KEY = os.environ.get("CG_SECRET_KEY", "YOUR_SECRET_KEY")
    BASE_URL = os.environ.get("CG_BASE_URL", "https://sandbox-api.craftgate.io")

    @classmethod
    def setUpClass(cls):
        options = RequestOptions(
            api_key=cls.API_KEY,
            secret_key=cls.SECRET_KEY,
            base_url=cls.BASE_URL
        )
        cls.onboarding = Craftgate(options).onboarding()

    def test_create_sub_merchant(self):
        request = CreateMemberRequest(
            is_buyer=False,
            is_sub_merchant=True,
            contact_name="Haluk",
            contact_surname="Demir",
            email="haluk.demir@example.com",
            phone_number="905551111111",
            iban="TR930006701000000001111111",
            legal_company_title="Dem Zeytinyağı Üretim Ltd. Şti.",
            name="Dem Zeytinyağı Üretim Ltd. Şti.",
            member_type=MemberType.LIMITED_OR_JOINT_STOCK_COMPANY,
            member_external_id=str(uuid.uuid4()),
            tax_number="1111111114",
            tax_office="Erenköy",
            address="Suadiye Mah. Örnek Cd. No:23, 34740 Kadıköy/İstanbul"
        )
        response = self.onboarding.create_member(request)
        print(vars(response))

        self.assertIsNotNone(response.id)
        self.assertEqual(request.contact_name, response.contact_name)
        self.assertEqual(request.contact_surname, response.contact_surname)
        self.assertEqual(request.email, response.email)
        self.assertEqual(request.phone_number, response.phone_number)
        self.assertEqual(request.iban, response.iban)
        self.assertEqual(request.legal_company_title, response.legal_company_title)
        self.assertEqual(request.name, response.name)
        self.assertEqual(request.member_type, response.member_type)
        self.assertEqual(request.member_external_id, response.member_external_id)
        self.assertEqual(request.tax_number, response.tax_number)
        self.assertEqual(request.tax_office, response.tax_office)
        self.assertEqual(request.address, response.address)

    def test_update_sub_merchant(self):
        member_id = 116210
        request = UpdateMemberRequest(
            is_buyer=False,
            is_sub_merchant=True,
            contact_name="Haluk",
            contact_surname="Demir",
            email="haluk.demir@example.com",
            phone_number="905551111111",
            legal_company_title="Dem Zeytinyağı Üretim Ltd. Şti.",
            name="Dem Zeytinyağı Üretim Ltd. Şti.",
            member_type=MemberType.LIMITED_OR_JOINT_STOCK_COMPANY,
            tax_number="1111111114",
            tax_office="Erenköy",
            address="Suadiye Mah. Örnek Cd. No:23, 34740 Kadıköy/İstanbul",
            iban="TR930006701000000001111111",
            settlement_earnings_destination=SettlementEarningsDestination.IBAN
        )
        response = self.onboarding.update_member(member_id, request)

        self.assertEqual(member_id, response.id)
        self.assertEqual(request.contact_name, response.contact_name)
        self.assertEqual(request.contact_surname, response.contact_surname)
        self.assertEqual(request.email, response.email)
        self.assertEqual(request.phone_number, response.phone_number)
        self.assertEqual(request.legal_company_title, response.legal_company_title)
        self.assertEqual(request.name, response.name)
        self.assertEqual(request.tax_number, response.tax_number)
        self.assertEqual(request.tax_office, response.tax_office)
        self.assertEqual(request.address, response.address)

    def test_retrieve_sub_merchant(self):
        member_id = 116210
        response = self.onboarding.retrieve_member(member_id)
        print(vars(response))
        self.assertEqual(member_id, response.id)

    def test_create_buyer(self):
        request = CreateMemberRequest(
            member_external_id=str(uuid.uuid4()),
            name="Haluk Demir",
            email="haluk.demir@example.com",
            phone_number="905551111111",
            address="Suadiye Mah. Örnek Cd. No:23, 34740 Kadıköy/İstanbul",
            contact_name="Haluk",
            contact_surname="Demir"
        )
        response = self.onboarding.create_member(request)

        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertTrue(response.is_buyer)
        self.assertEqual(request.member_external_id, response.member_external_id)
        self.assertEqual(request.email, response.email)
        self.assertEqual(request.phone_number, response.phone_number)
        self.assertEqual(request.name, response.name)

    def test_update_buyer(self):
        member_id = 116211
        request = UpdateMemberRequest(
            name="Haluk Demir",
            email="haluk.demir@example.com",
            phone_number="905551111112",
            address="Suadiye Mah. Örnek Cd. No:23, 34740 Kadıköy/İstanbul",
            contact_name="Haluk",
            contact_surname="Demir"
        )
        response = self.onboarding.update_member(member_id, request)

        print(vars(response))
        self.assertTrue(response.is_buyer)
        self.assertEqual(member_id, response.id)
        self.assertEqual(request.email, response.email)
        self.assertEqual(request.phone_number, response.phone_number)
        self.assertEqual(request.name, response.name)

    def test_retrieve_buyer(self):
        member_id = 116211
        response = self.onboarding.retrieve_member(member_id)

        print(vars(response))
        self.assertEqual(member_id, response.id)

    def test_search_members(self):
        request = SearchMembersRequest(
            member_ids={116210, 116211},
            name="Zeytinyağı Üretim"
        )
        response = self.onboarding.search_members(request)

        print(vars(response))
        self.assertTrue(len(response.items) > 0)

    def test_create_member_as_sub_merchant_and_buyer(self):
        request = CreateMemberRequest(
            is_buyer=True,
            is_sub_merchant=True,
            contact_name="Haluk",
            contact_surname="Demir",
            email="haluk.demir@example.com",
            phone_number="905551111111",
            iban="TR930006701000000001111111",
            legal_company_title="Dem Zeytinyağı Üretim Ltd. Şti.",
            name="Dem Zeytinyağı Üretim Ltd. Şti.",
            member_type=MemberType.LIMITED_OR_JOINT_STOCK_COMPANY,
            member_external_id=str(uuid.uuid4()),
            tax_number="1111111114",
            tax_office="Erenköy",
            address="Suadiye Mah. Örnek Cd. No:23,"
        )
        response = self.onboarding.create_member(request)

        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertEqual(request.contact_name, response.contact_name)
        self.assertEqual(request.contact_surname, response.contact_surname)
        self.assertEqual(request.email, response.email)
        self.assertEqual(request.phone_number, response.phone_number)
        self.assertEqual(request.iban, response.iban)
        self.assertEqual(request.legal_company_title, response.legal_company_title)
        self.assertEqual(request.name, response.name)
        self.assertEqual(request.member_type, response.member_type)
        self.assertEqual(request.member_external_id, response.member_external_id)
        self.assertEqual(request.tax_number, response.tax_number)
        self.assertEqual(request.tax_office, response.tax_office)
        self.assertEqual(request.address, response.address)

    def test_create_merchant(self):
        request = CreateMerchantRequest(
            name="newMerchant",
            legal_company_title="legalCompanyTitle",
            email="new_merchant1@merchant.com",
            website="www.merchant.com",
            contact_name="newName",
            contact_surname="newSurname",
            phone_number="905555555566",
            contact_phone_number="905555555566"
        )
        response = self.onboarding.create_merchant(request)

        print(vars(response))
        self.assertIsNotNone(response.id)
        self.assertEqual(request.name, response.name)
        self.assertEqual(len(response.merchant_api_credentials), 1)


if __name__ == "__main__":
    unittest.main()
