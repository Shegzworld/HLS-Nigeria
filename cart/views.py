from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart
from paystackapi.transaction import Transaction
# from django.contrib.auth.models import User
from django.conf import settings
import requests

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the product already exists in the user's cart
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}  # Set default quantity if creating a new item
    )

    if not created:
        # If the item already exists in the cart, increase the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:view')  # Redirect to cart view or another page as necessary


@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(Cart, id=item_id, user=request.user)
    item.delete()
    return redirect('')

@login_required
def checkout(request):
    cart_items = request.user.cart.all()
    total_amount = sum(item.total_price for item in cart_items)  # Calculate total price

    if request.method == "POST":
        # Initialize Paystack transaction
        response = Transaction.initialize({
            'email': request.user.email,
            'amount': int(total_amount * 100),  # Amount is in kobo
            'callback_url': 'https://www.hls.com.ng/cart/checkout/success/',  
        })

        if response['status']:
            return redirect(response['data']['authorization_url'])  # Redirect to Paystack for payment
        else:
            return render(request, 'cart/checkout.html', {'error': response['message']})
    # loggedUser = User.objects.all()
    # print(request.user)
    # print(loggedUser)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_amount': total_amount,
        'user':request.user
    })

@login_required
def payment_success(request):
    payment_reference = request.GET.get('reference')
    print(f"Payment Reference: {payment_reference}")

    if payment_reference:
        # Use your Paystack secret key to verify the transaction
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
        }
        url = f"https://api.paystack.co/transaction/verify/{payment_reference}"

        response = requests.get(url, headers=headers)
        result = response.json()  # Convert response to JSON

        print(f"Verification Response: {result}")

        if result['status']:
            # Transaction successful
            return render(request, 'payment_success.html', {
                'message': 'Payment was successful!',
                'payment_reference': payment_reference,
            })
        else:
            # Transaction not successful
            return render(request, 'payment_failure.html', {
                'message': 'Payment was not successful!',
            })
    else:
        return render(request, 'payment_failure.html', {
            'message': 'Payment reference is missing.',
        })