from django.shortcuts import render
from .serializers import ItemSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Item, User

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer    