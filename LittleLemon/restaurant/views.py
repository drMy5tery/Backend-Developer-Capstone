from django.shortcuts import render
from .models import Menu
from .serializers import Menuserializer
from rest_framework import generics

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = Menuserializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = Menuserializer