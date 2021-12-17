from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from .models import *

# Create your views here.
class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class Purchase_OrderViewSet(viewsets.ModelViewSet):
    queryset = Purchase_Order.objects.all().aggregate()
    serializer_class = Purchase_OrderSerializer
    

class Plain_Carton_Line_ItemViewSet(viewsets.ModelViewSet):
    queryset = Plain_Carton_Line_Item.objects.all()
    serializer_class = Plain_Carton_Line_ItemSerializer


