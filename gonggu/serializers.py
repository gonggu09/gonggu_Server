from rest_framework import serializers
from .models import User, Item

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    sellerId = serializers.CharField(source='sellerId.name', read_only=True)
    #profile_photo=serializers.ImageField(source='sellerId.profile_photo', read_only=True)

    class Meta:
        model = Item
        fields = ['sellerId', 'productName', 'price', 'productImg', 'startDate', 'endDate', 'url']