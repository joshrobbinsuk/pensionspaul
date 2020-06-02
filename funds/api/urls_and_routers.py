from rest_framework import routers
from funds.api import views

router = routers.DefaultRouter()

router.register(r'funds', views.FundViewSet)
