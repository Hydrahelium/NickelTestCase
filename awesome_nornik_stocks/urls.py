from django.urls import path, include
from .views import StockList


urlpatterns = [
    path('', StockList.as_view(), name='stocks'),
]
