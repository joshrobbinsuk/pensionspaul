from django.shortcuts import render
from funds.models import Fund
from funds.analysis_methods import method_drawdown, method_growth
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from funds.forms import AnalysisForm, FundForm, FundForm2
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import csv


class FundDetailView(LoginRequiredMixin, generic.DetailView):
    model = Fund


class FundListView(LoginRequiredMixin, generic.ListView):
    model = Fund


@method_decorator(staff_member_required, name="dispatch")
class FundCreate(LoginRequiredMixin, CreateView):
    model = Fund
    fields = "__all__"


@method_decorator(staff_member_required, name="dispatch")
class FundUpdate(LoginRequiredMixin, UpdateView):
    model = Fund
    fields = "__all__"


@method_decorator(staff_member_required, name="dispatch")
class FundDelete(LoginRequiredMixin, DeleteView):
    model = Fund
    success_url = reverse_lazy("fund-list")


@login_required
def CompareFunds(request):
    form_a = AnalysisForm(request.GET)
    if request.GET != {}:
        pot_size = int(request.GET["pot_size"])
        years = int(request.GET["years"])
        drawdown = int(request.GET["drawdown"])
        Fund.starting_pot = pot_size
        Fund.comparison_years = years
        Fund.drawdown_pc = drawdown

        funds = sorted(Fund.objects.all(), key=lambda p: p.daddy_property, reverse=True)
        for f in funds:
            f.starting_pot = pot_size
            f.costs_accrued = 0
            f.fund_costs = 0
            f.platform_costs = 0
            f.growth_accrued = 0
            f.drawn_out = 0

        return render(
            request,
            "compare_funds.html",
            {"form": form_a, "pot_size": pot_size, "years": years, "funds": funds},
        )

    else:
        form_a = AnalysisForm()
        return render(request, "compare_funds.html", {"form": form_a})


@login_required
def DetailedFund(request):
    form = FundForm2(request.GET)
    if request.GET:
        brand_id = request.GET["brand"]
        pot_size = int(request.GET["pot_size"])
        drawdown = int(request.GET["drawdown"])
        fund = Fund.objects.filter(id=brand_id).get()
        fund.starting_pot = pot_size
        fund.drawdown_pc = drawdown
        fund.mummy_method()

        brand = fund.brand
        if "csv" in request.GET:
            fund = Fund.objects.filter(brand=brand).get()
            fund.starting_pot = pot_size
            fund.drawdown_pc = drawdown
            fund.mummy_method()
            response = HttpResponse(content_type="text/csv")
            writer = csv.writer(response)
            filename_ = str(brand) + str(pot_size)
            writer.writerow(
                [
                    "Year",
                    "Pot",
                    "After setup costs",
                    "After fixed start costs",
                    "After drawdown",
                    "After ongoing costs",
                    "After growth",
                ]
            )
            _filename = (
                str(brand) + "_£" + str(pot_size) + "_%" + str(drawdown) + ".csv"
            )
            for tup in fund.final_tuple:
                writer.writerow(
                    [tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6]]
                )
            response["Content-Disposition"] = "attachment; filename=" + _filename
            return response

        return render(request, "detail_fund.html", {"form": form, "fund": fund,})

    else:
        form = FundForm2()
        return render(request, "detail_fund.html", {"form": form})
