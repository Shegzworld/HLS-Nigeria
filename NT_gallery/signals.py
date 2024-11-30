from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductReview
from user.models import Notification

@receiver(post_save, sender=ProductReview)
def notify_subscribers_on_new_review(sender, instance, created, **kwargs):
    if created:  # Only notify on new reviews
        product = instance.product
        writer = instance.writer
        subscribers = product.subscribers.all()  # Get all subscriptions for the product
        
        # Notify each subscriber
        for subscription in subscribers:
            if subscription.user != writer:  # Avoid notifying the review writer
                Notification.objects.create(
                    user=subscription.user,
                    message=f"Product '{product.name}' has a new review by {writer.username}. Check it now!"
                )

                # Update the subscriber's unread notification count
                user_profile = subscription.user.profile
                user_profile.new_notifications_count += 1
                user_profile.save()
