from .adapter import *
from .exception import *
from .model import *
from .net import *
from .request import *
from .response import *
from .utils import *
from request_options import RequestOptions

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

    def payment(self):
        return PaymentAdapter(self.options)

    def bank_account_tracking(self):
        return BankAccountTrackingAdapter(self.options)

    def bkm_express_payment(self):
        return BkmExpressPaymentAdapter(self.options)

    def file_reporting(self):
        return FileReportingAdapter(self.options)

    def fraud(self):
        return FraudAdapter(self.options)

    def hook(self):
        return HookAdapter(self.options)

    def installment(self):
        return InstallmentAdapter(self.options)

    def juzdan_payment(self):
        return JuzdanPaymentAdapter(self.options)

    def masterpass_payment(self):
        return MasterpassPaymentAdapter(self.options)

    def merchant(self):
        return MerchantAdapter(self.options)

    def merchant_apm(self):
        return MerchantApmAdapter(self.options)

    def onboarding(self):
        return OnboardingAdapter(self.options)

    def pay_by_link(self):
        return PayByLinkAdapter(self.options)

    def payment_reporting(self):
        return PaymentReportingAdapter(self.options)

    def payment_token(self):
        return PaymentTokenAdapter(self.options)

    def settlement(self):
        return SettlementAdapter(self.options)

    def settlement_reporting(self):
        return SettlementReportingAdapter(self.options)

    def wallet(self):
        return WalletAdapter(self.options)
