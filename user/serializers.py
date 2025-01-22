from rest_framework import serializers
from .models import Principal, Benfek

class BenfekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benfek
        fields = "__all__"

class PrincipalSerializer(serializers.ModelSerializer):
    beneficiaries = BenfekSerializer(many=True, read_only=True)

    class Meta:
        model = Principal
        fields = "__all__"
