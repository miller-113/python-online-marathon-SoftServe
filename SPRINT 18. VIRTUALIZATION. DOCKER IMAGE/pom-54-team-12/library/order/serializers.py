from rest_framework import serializers
from .models import Order
from rest_framework import permissions


class OrdersSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    book = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['id', 'book', 'user', 'created_at', 'plated_end_at']

