from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction, MonthlyTransactionSummary

@receiver(post_save, sender=Transaction)
def update_monthly_transaction_summary(sender, instance, **kwargs):
    if instance.transaction_type == 'withdrawal':
        month = instance.date.month
        year = instance.date.year
        user = instance.wallet.user

        summary, created = MonthlyTransactionSummary.objects.get_or_create(
            user=user,
            year=year,
            month=month,
        )

        summary.withdrawals_count = Transaction.objects.filter(
            wallet=instance.wallet,
            transaction_type='withdrawal',
            date__year=year,
            date__month=month
        ).count()

        summary.save()
