"""happy_homes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from happy_homes.rentals.views.auth import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('happy_homes.rentals.urls')),
    path('auth/', include('rest_framework.urls')),

]

"""path('gettoken/', obtain_auth_token),"""


"""
so this was api based token generation
path('gettoken/', CustomAuthToken.as_view()),
generate token -> http POST http://127.0.0.1:8000/gettoken/ username="eric" password="Satyamsingh@123" 
"""

"""
so after api based token generation we will try create token through signal 
in this case as soon as we create a new user a new token will be created for that user

"""

