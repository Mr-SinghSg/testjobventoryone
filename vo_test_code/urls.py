from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from test_app_1 import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('warehouse',views.WarehouseViewSet,basename='warehouse')
router.register('purchase',views.Purchase_OrderViewSet,basename='purchase')
router.register('plain',views.Plain_Carton_Line_ItemViewSet,basename='plain')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]