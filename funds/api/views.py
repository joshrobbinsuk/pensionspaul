from rest_framework import viewsets
from funds.models import Fund
from funds.api.serializers import FundSerializer

class FundViewSet(viewsets.ModelViewSet):
	queryset = Fund.objects.all()
	serializer_class = FundSerializer



