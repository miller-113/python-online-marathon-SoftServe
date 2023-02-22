from rest_framework import serializers
from .models import CustomUser
from order.serializers import OrdersSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    orderDetails = OrdersSerializer(read_only=True, many=True,
                                    source="order_set")

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'middle_name',
                  'role', 'is_active', 'is_staff', 'is_superuser',
                  'orderDetails', 'order_set']


# class CustomUserOrderSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Order
#         # fields = ['book', 'user', 'created_at', 'plated_end_at']
#         fields = '__all__'
