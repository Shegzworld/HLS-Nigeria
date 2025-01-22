from django.test import TestCase

# Create your tests here.
from .models import Payment

class PaymentTest(TestCase):
    def setUp(self):
        self.payment = Payment.objects.create(
            transaction_id='12345',
            amount=1000,
            status='success',
            currency='NGN',
            description='Payment for subscription',
            customer_name='John Doe',
            customer_email='johndoe@example.com',
            customer_phone='08012345678',
        )
    
    def test_payment_str_representation(self):
        self.assertEqual(str(self.payment), 'Payment for subscription - John Doe')
        self.assertEqual(self.payment.get_status_display(), 'Success')
        self.assertEqual(self.payment.get_currency_display(), 'NGN')
        self.assertEqual(self.payment.get_status_color(), 'success')
        self.assertEqual(self.payment.get_currency_symbol(), '��')
        self.assertEqual(self.payment.get_status_icon(), 'fa-check')
        self.assertEqual(self.payment.get_currency_icon(), 'fa-flag-ng')
        self.assertEqual(self.payment.get_status_badge(), 'badge badge-success')
        self.assertEqual(self.payment.get_currency_badge(), 'badge badge-primary')
        self.assertEqual(self.payment.get_status_class(), 'success')
        self.assertEqual(self.payment.get_currency_class(), 'primary')
        self.assertEqual(self.payment.get_status_label(), 'Label label-success')
        self.assertEqual(self.payment.get_currency_label(), 'Label label-primary')
        self.assertEqual(self.payment.get_status_color_gradient(), 'gradient-success')

    def test_payment_status_color(self):
        self.assertEqual(self.payment.get_status_color(), 'success')
        self.assertEqual(self.payment.get_currency_color(), 'primary')
        self.assertEqual(self.payment.get_status_color_gradient(), 'gradient-success')
    