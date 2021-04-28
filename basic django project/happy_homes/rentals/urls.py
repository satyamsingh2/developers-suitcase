from django.urls import path
from .views.owners import OwnerDetailView, OwnerListView
from .views.property import PropertyListView, PropertyDetailView


urlpatterns = [
    path('owner/', OwnerListView.as_view(), name='owner-list'),
    path('owner/<int:owner_id>/', OwnerDetailView.as_view(), name='owner-detail'),
    path('property/', PropertyListView.as_view(), name='property-list'),
    path('property/<int:property_id>/', PropertyDetailView.as_view(), name='property-detail'),
]