# cart/management/commands/seed_cart.py
from django.core.management.base import BaseCommand
from cart.models import Cart, Product  # Adjust the import according to your models
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed the database with dummy cart data'

    def handle(self, *args, **options):
        # Get or create a user
        user, created = User.objects.get_or_create(username='fola', defaults={'password': 'Oluwabunmi13#'})
        if created:
            user.set_password('password')  # Set the password for the created user
            user.save()

        # Create dummy products
        product_names = ['Product 1', 'Product 2', 'Product 3']
        products = []

        for name in product_names:
            product = Product.objects.create(
                name=name,
                price=10.00,  # Example price
                description=f'Description for {name}'
            )
            products.append(product)

        # Create a cart and add items to it
        for product in products:
            Cart.objects.create(
                user=user,
                product=product,
                quantity=2  # Example quantity
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the cart with dummy data'))
