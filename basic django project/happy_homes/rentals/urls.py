from django.urls import path
from .views.owners import OwnerDetailView, OwnerListView
from .views.property import PropertyListView, PropertyDetailView
from .views.django_based_auth.register import register_page, login_page, logout_page


urlpatterns = [
    path('owner/', OwnerListView.as_view(), name='owner-list'),
    path('owner/<int:owner_id>/', OwnerDetailView.as_view(), name='owner-detail'),
    path('property/', PropertyListView.as_view(), name='property-list'),
    path('property/<int:property_id>/', PropertyDetailView.as_view(), name='property-detail'),


]

"""path('register/', register_page, name="register"),
   path('login/', login_page, name="login"),
   path('logout/', logout_page, name="logout"),"""