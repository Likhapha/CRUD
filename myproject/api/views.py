

from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def home(request):
    return HttpResponse("<h1>Welcome to the API!</h1>")
