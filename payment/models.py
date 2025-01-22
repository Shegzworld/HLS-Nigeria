from django.db import models

# Create your models here.

class Payment(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=200)
    transaction_id = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    customer_id = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Payment #{self.id} for Order #{self.order_id}"
    
    class Meta:
        verbose_name_plural = "Payments"

