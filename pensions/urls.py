"""pensions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from funds import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('fund/<int:pk>/', views.FundDetailView.as_view(), name='fund-detail'),
    path('allfunds/', views.FundListView.as_view(),name='fund-list'),

    path('newfund', views.FundCreate.as_view(), name='new-fund'),
    path('fund/<int:pk>/update/', views.FundUpdate.as_view(),name='fund-update'),
    path('fund/<int:pk>/delete/', views.FundDelete.as_view(),name='fund-delete'),

    #path('analyse/', views.Analyse2,name='analyse'),
    path('comparefunds/', views.CompareFunds, name='compare-funds'),
    path('detailedview/', views.DetailedFund, name='detailed-view'),

    path('accounts/', include('django.contrib.auth.urls')),
# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']


    path('formtest/', views.formtest,name='formtest'),
] 