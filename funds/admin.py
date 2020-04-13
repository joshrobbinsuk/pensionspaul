from django.contrib import admin

# Register your models here.
from .models import Fund

# #admin.site.register(Fund)


# class FundAdmin(admin.ModelAdmin):
#     list_display = ('brand', 'setup_costs', 'fixed_costs_year_start', 'fixed_costs_ongoing','band_1_lower',
#     	'band_1_upper','band_1_rate')
#     fields = ['brand', 'setup_costs', 'fixed_costs_year_start', 'fixed_costs_ongoing', 
#     ('band_1_lower', 'band_1_upper','band_1_rate')]


# admin.site.register(Fund,FundAdmin)