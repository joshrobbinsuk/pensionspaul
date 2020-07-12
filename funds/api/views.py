from rest_framework import viewsets, generics
from funds.models import Fund
from funds.api.serializers import FundSerializer, CompareFundSerializer
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from rest_framework.response import Response
from rest_framework.documentation import include_docs_urls
from django.contrib.auth.decorators import login_required


@login_required
@api_view(["GET"])
def compare_funds_api(request):
    data = request.query_params
    serializer = CompareFundSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    Fund.starting_pot = int(data["potsize"])
    Fund.comparison_years = int(data["years"])
    Fund.drawdown_pc = int(data["drawdown"])

    def get_dict_from_fund(f):
        output = {
            "brand": f.brand,
            "final_pot": f.daddy_method(),
            "fund_costs": f.fund_costs,
            "total_costs": f.total_costs(),
            "drawn_out": f.drawn_out,
            "growth_accrued": f.growth_accrued,
        }
        return output

    final_output = [get_dict_from_fund(f) for f in Fund.objects.all()]
    final_output = sorted(
        final_output, key=lambda fund: fund["final_pot"], reverse=True
    )

    return Response(final_output)


# UNUSED VIEWS

# class CompareFundsList(generics.ListAPIView):
# 	serializer_class = FundSerializer
# 	queryset = Fund.objects.all()

# class FundViewSet(viewsets.ReadOnlyModelViewSet):
# 	queryset = Fund.objects.all()
# 	serializer_class = FundSerializer
# 	permission_classes = [IsAccountAdminOrReadOnly]
