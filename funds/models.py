from django.db import models
from django.urls import reverse

#from analysis_methods import method_drawdown, method_growth

from decimal import Decimal
TWOPLACES = Decimal('1.00')


# Create your models here.


class Fund(models.Model):
	brand = models.CharField(max_length=100)

	FUND_CHOICES = (
	('p', 'Pension Company'),
	('f', 'Fund Supermarket')
		)
	fund_type = models.CharField(max_length=1,choices=FUND_CHOICES,default='p')
	setup_costs = models.DecimalField(max_digits=9, decimal_places=2,default=0)
	fixed_costs_year_start = models.DecimalField(max_digits=9, decimal_places=2,default=0)
	fixed_costs_ongoing = models.DecimalField(max_digits=9, decimal_places=2,default=0)
	PLATFORM_CHOICES = (
		('itb', 'ITB'),
		('wf', 'Whole Fund'),
		('n', 'Neither')
		)
	platform_type = models.CharField(max_length=3,choices=PLATFORM_CHOICES,default='itb')	
	band_1_lower = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True, default=0)
	band_1_rate = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True)
	end_1_band_2 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True)
	band_2_rate = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True)
	end_2_band_3 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True)
	band_3_rate = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True)
	end_3_band_4 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True)
	band_4_rate = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True)
	end_4_band_5 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True)
	band_5_rate = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True)
	end_5_band_6 = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True)
	band_6_rate = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank = True)

	def __str__(self):
		return self.brand

	def get_absolute_url(self):
		return reverse('fund-detail', kwargs={'pk':self.pk})

	def get_fields(self):
		return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

	#####################

	starting_pot = None

	def method_setup_costs(self):
		if self.tracking_years == 1:
			new_pot = self.starting_pot - self.setup_costs
			return new_pot
		else:
			return '-'

	def method_fixed_start_costs(self):
		if self.tracking_years == 1:
			new_pot = self.method_setup_costs() - self.fixed_costs_year_start
			return new_pot
		else:
			new_pot = self.starting_pot - self.fixed_costs_year_start
			return new_pot

	def method_drawdown(self):
		new_pot = self.method_fixed_start_costs() * Decimal(95)/100
		return new_pot.quantize(TWOPLACES)

	def method_ongoing_costs(self):
		pot = self.method_drawdown()
		original_pot = pot

		if self.platform_type == 'wf':
			platform_costs = pot * self.band_1_rate/100
		
			if self.end_1_band_2 is not None: 
				if pot > self.end_1_band_2:
					platform_costs = pot * self.band_2_rate/100	

			if self.end_2_band_3 is not None: 
				if pot > self.end_2_band_3:
					platform_costs = pot * self.band_3_rate/100

			if self.end_3_band_4 is not None: 
				if pot > self.end_3_band_4:
					platform_costs = pot * self.band_4_rate/100

			if self.end_4_band_5 is not None: 
				if pot > self.end_4_band_5:
					platform_costs = pot * self.band_5_rate/100

			if self.end_5_band_6 is not None: 
				if pot > self.end_5_band_6:
					platform_costs = pot * self.band_6_rate/100

		elif self.platform_type == 'itb':
			platform_costs = 0
			if self.end_5_band_6 is not None: 
				if pot > self.end_5_band_6:
					platform_costs += (pot - self.end_5_band_6) * self.band_6_rate/100
					pot = self.end_5_band_6

			if self.end_4_band_5 is not None: 
				if pot > self.end_4_band_5:
					platform_costs += (pot - self.end_4_band_6) * self.band_5_rate/100
					pot = self.end_4_band_5

			if self.end_3_band_4 is not None: 
				if pot > self.end_3_band_4:
					platform_costs += (pot - self.end_3_band_4) * self.band_4_rate/100
					pot = self.end_3_band_4

			if self.end_2_band_3 is not None: 
				if pot > self.end_2_band_3:
					platform_costs += (pot - self.end_2_band_3) * self.band_3_rate/100
					pot = self.end_2_band_3

			if self.end_1_band_2 is not None: 
				if pot > self.end_1_band_2:
					platform_costs += (pot - self.end_1_band_2) * self.band_2_rate/100
					pot = self.end_1_band_2
			platform_costs += pot * self.band_1_rate/100

		else:
			platform_costs = 0

		new_pot = original_pot - platform_costs - self.fixed_costs_ongoing
		new_pot_rounded = new_pot.quantize(TWOPLACES)
		return new_pot_rounded

	def method_growth(self):
		new_pot = self.method_ongoing_costs() * Decimal(103.3)/100
		return new_pot.quantize(TWOPLACES)

###### DADDY METHOD
	
	tracking_years = None
	comparison_years = None
    

	def daddy_method(self):
		self.tracking_years = 1
		while self.tracking_years <= self.comparison_years:
			new_pot = self.method_growth()
			self.starting_pot = new_pot

			self.tracking_years += 1

		return(new_pot)

	@property
	def daddy_property(self):
		return self.daddy_method()
	
	daddy_property = property(daddy_method)


	def mummy_method(self):
		self.tracking_years = 1
		self.pot_tracker = []
		self.setup_tracker = []
		self.fixed_tracker = []
		self.drawdown_tracker = []
		self.ongoing_tracker = []
		self.growth_tracker = []
		self.years_tracker = []
		while self.tracking_years < 50:
			self.years_tracker.append(self.tracking_years)
			self.pot_tracker.append(self.starting_pot)
			self.setup_tracker.append(self.method_setup_costs())
			self.fixed_tracker.append(self.method_fixed_start_costs())
			self.drawdown_tracker.append(self.method_drawdown())
			self.ongoing_tracker.append(self.method_drawdown())
			self.growth_tracker.append(self.method_growth())
			self.starting_pot = self.method_growth()

			self.tracking_years += 1

		self.final_tuple = list(zip(self.years_tracker, self.pot_tracker,self.setup_tracker,self.fixed_tracker,
			self.drawdown_tracker,self.ongoing_tracker,self.growth_tracker))


	years_tracker = []
	pot_tracker = []
	setup_tracker = []
	fixed_tracker = []
	drawdown_tracker = []
	ongoing_tracker = []
	growth_tracker = []








