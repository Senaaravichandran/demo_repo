# Configuration settings for payment gateway integration
class PaymentGatewayConfig:
    def __init__(self):
        self.payment_gateway_url = "https://example.com/payment/gateway"
        self.payment_gateway_api_key = "your_api_key_here"
        self.payment_gateway_secret_key = "your_secret_key_here"

    def update_config(self, payment_gateway_url=None, payment_gateway_api_key=None, payment_gateway_secret_key=None):
        if payment_gateway_url:
            self.payment_gateway_url = payment_gateway_url
        if payment_gateway_api_key:
            self.payment_gateway_api_key = payment_gateway_api_key
        if payment_gateway_secret_key:
            self.payment_gateway_secret_key = payment_gateway_secret_key

# Initialize payment gateway configuration
payment_config = PaymentGatewayConfig()