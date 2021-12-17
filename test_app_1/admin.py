from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(SKU)
admin.site.register(Warehouse)
admin.site.register(Purchase_Order)
admin.site.register(Plain_Carton_Line_Item)

