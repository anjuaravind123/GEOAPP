from rest_framework import serializers
from .models import CustomerBookmark


class custbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBookmark
        fields = "__all__"
