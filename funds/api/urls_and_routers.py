from rest_framework import routers
from .views import compare_funds_api  # CompareFundsList     # FundViewSet
from django.urls import path, include

# router = routers.DefaultRouter()
# router.register(r'funds', FundViewSet)

urls = [
    path("", compare_funds_api, name="api"),
]
