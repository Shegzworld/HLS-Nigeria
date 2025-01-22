
from django.shortcuts import redirect
from django.http import JsonResponse
from .utils.paystack import Paystack
from .models import Payment
from django.views.decorators.csrf import csrf_exempt
import json

def initialize_payment(request):
    if request.method == "POST":
        email = request.POST.get("email")
        amount = float(request.POST.get("amount"))
        paystack = Paystack()
        response = paystack.initialize_transaction(amount, email)
        if response.get("status"):
            authorization_url = response["data"]["authorization_url"]
            return redirect(authorization_url)
        return JsonResponse({"error": "Failed to initialize payment"}, status=400)


def verify_payment(request):
    reference = request.GET.get("reference")
    paystack = Paystack()
    response = paystack.verify_transaction(reference)

    if response.get("status"):
        data = response.get("data", {})
        Payment.objects.create(
            order_id=data["metadata"].get("order_id"),
            payment_method="Paystack",
            transaction_id=data["id"],
            amount=data["amount"] / 100,  # Convert kobo to naira
            payment_status=True,
            customer_id=data["customer"]["id"],
        )
        return JsonResponse({"message": "Payment successful"})
    return JsonResponse({"error": "Payment verification failed"}, status=400)



@csrf_exempt
def paystack_webhook(request):
    payload = json.loads(request.body)
    event = payload.get("event")
    if event == "charge.success":
        data = payload.get("data", {})
        Payment.objects.filter(transaction_id=data["id"]).update(payment_status=True)
    return JsonResponse({"status": "success"})
