from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
import logging 
from .models import ProductReview, ProductSubscription
logger = logging.getLogger(__name__)

@receiver(post_save, sender=ProductReview)
def notify_subscribers(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        subscribers = ProductSubscription.objects.filter(product=product)
        
        for subscription in subscribers:
            user = subscription.user
            subject = f"New review on {product.name}"
            message = f"Hello {user.username},\n\nA new review has been posted for the product {product.name}:\n\n{instance.comment}\n\nBest regards,\nYour Shop"
            
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
                logger.info(f"Email sent to {user.email} for product {product.name}")
            except Exception as e:
                logger.error(f"Failed to send email to {user.email} for product {product.name}: {e}")
