from .adapter import *
from .exception import *
from .model import *
from .net import *
from .request import *
from .response import *
from .utils import *
from .request_options import RequestOptions

class Craftgate:

    def __init__(self, options):
        if isinstance(options, dict):
            options = RequestOptions(
                api_key= options.get('api_key'),
                secret_key= options.get('secret_key'),
                base_url= options.get('base_url'),
                language= options.get('language', None)
            )

        if not isinstance(options, RequestOptions):
            raise ValueError("options must be either a request_options.py instance or a dictionary")

        self.options = options

    def payment(self) -> PaymentAdapter:
        return PaymentAdapter(self.options)

    def bank_account_tracking(self) -> BankAccountTrackingAdapter:
        return BankAccountTrackingAdapter(self.options)

    def bkm_express_payment(self) -> BkmExpressPaymentAdapter:
        return BkmExpressPaymentAdapter(self.options)

    def file_reporting(self) -> FileReportingAdapter:
        return FileReportingAdapter(self.options)

    def fraud(self) -> FraudAdapter:
        return FraudAdapter(self.options)

    def hook(self) -> HookAdapter:
        return HookAdapter(self.options)

    def installment(self) -> InstallmentAdapter:
        return InstallmentAdapter(self.options)

    def juzdan_payment(self) -> JuzdanPaymentAdapter:
        return JuzdanPaymentAdapter(self.options)

    def masterpass_payment(self) -> MasterpassPaymentAdapter:
        return MasterpassPaymentAdapter(self.options)

    def merchant(self) -> MerchantAdapter:
        return MerchantAdapter(self.options)

    def merchant_apm(self) -> MerchantApmAdapter:
        return MerchantApmAdapter(self.options)

    def onboarding(self) -> OnboardingAdapter:
        return OnboardingAdapter(self.options)

    def pay_by_link(self) -> PayByLinkAdapter:
        return PayByLinkAdapter(self.options)

    def payment_reporting(self) -> PaymentReportingAdapter:
        return PaymentReportingAdapter(self.options)

    def payment_token(self) -> PaymentTokenAdapter:
        return PaymentTokenAdapter(self.options)

    def settlement(self) -> SettlementAdapter:
        return SettlementAdapter(self.options)

    def settlement_reporting(self) -> SettlementReportingAdapter:
        return SettlementReportingAdapter(self.options)

    def wallet(self) -> WalletAdapter:
        return WalletAdapter(self.options)

    def meal_voucher_card_tokenization(self) -> MealVoucherCardTokenizationAdapter:
        return MealVoucherCardTokenizationAdapter(self.options)
