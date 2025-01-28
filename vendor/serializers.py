from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Wallet, Transaction, Customer, Supplement, Article, Podcast,Health_Condition

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class SupplementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplement
        fields = ['id', 'name', 'price', 'expiry', 'image']  
        read_only_fields = ['user']  # Ensure the 'user' field is read-only

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'

class HealthConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_Condition
        fields = ['id', 'benfek', 'code', 'phone', 'current_medication','have_health_condition','health_condition','allergies','scary_issue']  
        read_only_fields = ['user']  # Ensure the 'user' field is read-only