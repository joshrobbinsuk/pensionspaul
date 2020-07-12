from django.contrib import admin
from django.urls import path, include
from funds import views
from funds.api.urls_and_routers import urls as api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("allfunds/", views.FundListView.as_view(), name="fund-list"),
    path("", views.FundListView.as_view(), name="fund-list-alt"),
    path("fund/<int:pk>/", views.FundDetailView.as_view(), name="fund-detail"),
    path("newfund", views.FundCreate.as_view(), name="new-fund"),
    path("fund/<int:pk>/update/", views.FundUpdate.as_view(), name="fund-update"),
    path("fund/<int:pk>/delete/", views.FundDelete.as_view(), name="fund-delete"),
    path("comparefunds/", views.CompareFunds, name="compare-funds"),
    path("detailedview/", views.DetailedFund, name="detailed-view"),
    path("accounts/", include("django.contrib.auth.urls")),
    # accounts/ login/ [name='login']
    # accounts/ logout/ [name='logout']
    # accounts/ password_change/ [name='password_change']
    # accounts/ password_change/done/ [name='password_change_done']
    # accounts/ password_reset/ [name='password_reset']
    # accounts/ password_reset/done/ [name='password_reset_done']
    # accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/ reset/done/ [name='password_reset_complete']
    path("api/", include(api_urls)),
]
