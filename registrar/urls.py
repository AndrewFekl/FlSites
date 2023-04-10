from django.contrib import admin
from django.urls import path
from .views import OrganizationtListView, OrganizationDetailView, AddOrganizationView

urlpatterns = [
    path('org/', OrganizationtListView.as_view(), name='organizations'),
    path('org/<int:pk>/', OrganizationDetailView.as_view(), name='organization'),
    path('org/add/', AddOrganizationView.as_view(), name='add_organization'),
    ]
