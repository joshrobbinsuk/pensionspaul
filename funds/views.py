from django.shortcuts import render


# Create your views here.
from funds.models import Fund

from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect, HttpResponse
from funds.forms import AnalysisForm, FundForm, FundForm2

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

import csv


class FundDetailView(LoginRequiredMixin,generic.DetailView):
	model = Fund

class FundListView(LoginRequiredMixin,generic.ListView):
	model = Fund

##############################

class FundCreate(LoginRequiredMixin,CreateView):
	model = Fund
	fields = '__all__'
	#initial = {'date_of_death': '05/01/2018'}


class FundUpdate(LoginRequiredMixin,UpdateView):
	model = Fund
	fields = '__all__'

class FundDelete(LoginRequiredMixin,DeleteView):
	model = Fund
	success_url = reverse_lazy('fund-list')

##############################
from .models import Fund
from .analysis_methods import method_drawdown, method_growth

# @login_required
# def Analyse2(request):
# 	form_a = AnalysisForm(request.GET)
# 	if request.GET != {}:
# 		pot_size =  int(request.GET['pot_size'])
# 		years = int(request.GET['years'])

# 		Fund.starting_pot = pot_size
# 		funds = Fund.objects.all()

# 		return render(request, 'analyse_funds.html', {'form': form_a,'pot_size':pot_size, 'years':years, 'funds':funds})
	
# 	else:  # render this to a different template entirely
# 		form_a = AnalysisForm()
# 		return render(request, 'analyse_funds.html', {'form': form_a})

@login_required
def CompareFunds(request):
	form_a = AnalysisForm(request.GET)
	if request.GET != {}:
		pot_size =  int(request.GET['pot_size'])
		years = int(request.GET['years'])
		Fund.starting_pot = pot_size
		Fund.comparison_years = years

		#funds = Fund.objects.all()
		funds = sorted(Fund.objects.all(), key=lambda p: p.daddy_property, reverse = True)
		for f in funds:
			f.starting_pot = pot_size
			f.costs_accrued = 0
			f.fund_costs = 0

		return render(request, 'compare_funds.html', {'form': form_a,'pot_size':pot_size, 'years':years, 'funds':funds})
	
	else:  # render this to a different template entirely
		form_a = AnalysisForm()
		return render(request, 'compare_funds.html', {'form': form_a})

@login_required
def DetailedFund(request):
	form = FundForm2(request.GET)
	if request.GET:
		brand = request.GET['brand']
		pot_size = int(request.GET['pot_size'])
		fund = Fund.objects.filter(brand = brand).get()
		fund.starting_pot = pot_size
		fund.mummy_method()

		if 'csv' in request.GET:
			fund = Fund.objects.filter(brand = brand).get()
			fund.starting_pot = pot_size
			fund.mummy_method()
			response = HttpResponse(content_type='text/csv')
			writer = csv.writer(response)
			filename_ = str(brand) + str(pot_size)
			writer.writerow(['Year','Pot','After setup costs','After fixed start costs','After drawdown',
								'After ongoing costs','After growth'])
			_filename = str(brand) + "_£" + str(pot_size)
			for tup in fund.final_tuple:
				writer.writerow([tup[0],tup[1],tup[2],tup[3],tup[4],tup[5],tup[6]])
			response['Content-Disposition'] = 'attachment; filename=' + _filename
			return response

		return render(request, 'detail_fund.html', {'form': form, 'fund':fund,})
	
	else:  # render this to a different template entirely
		form = FundForm2()
		return render(request, 'detail_fund.html', {'form': form})




###########################

# add dynamically - didn't work!
@login_required
def Analyse(request):
	form_a = AnalysisForm(request.GET)
	if request.GET != {}:
		pot_size =  request.GET['pot_size']
		years = request.GET['years']

		Fund.after_setup = property(lambda self: self.method_setup_costs(int(pot_size)))
		Fund.after_fixed_start = property(lambda self: self.method_fixed_start_costs(self.after_setup))
		Fund.after_drawdown = property(lambda self: method_drawdown(self.after_fixed_start))
		Fund.after_ongoing = property(lambda self: self.method_ongoing_costs(self.after_drawdown))
		Fund.after_growth = property(lambda self: method_growth(self.after_ongoing))

		funds = Fund.objects.all()
		return render(request, 'analyse_funds.html', {'form': form_a,'pot_size_var':pot_size, 'years_var':years, 'funds':funds})
	
	else:  # render this to a different template entirely
		form_a = AnalysisForm()
		return render(request, 'analyse_funds.html', {'form': form_a})



@login_required
def formtest(request):
	print(request.GET)
	return render(request, 'test_form.html')

