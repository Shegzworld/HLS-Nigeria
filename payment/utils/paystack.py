# payments/utils/paystack.py
import requests
from django.conf import settings

class Paystack:
    PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
    PAYSTACK_BASE_URL = "https://api.paystack.co"

    @staticmethod
    def initialize_transaction(amount, email):
        url = f"{Paystack.PAYSTACK_BASE_URL}/transaction/initialize"
        headers = {
            "Authorization": f"Bearer {Paystack.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "email": email,
            "amount": int(amount * 100),  # Paystack expects amount in kobo
        }
        response = requests.post(url, json=data, headers=headers)
        return response.json()

    @staticmethod
    def verify_transaction(reference):
        url = f"{Paystack.PAYSTACK_BASE_URL}/transaction/verify/{reference}"
        headers = {
            "Authorization": f"Bearer {Paystack.PAYSTACK_SECRET_KEY}",
        }
        response = requests.get(url, headers=headers)
        return response.json()
