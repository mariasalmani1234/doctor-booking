from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import TokenRefreshView

from accounts.token_views import CustomTokenObtainPairView


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        'api/',
        include('doctors.urls')
    ),

    path(
        'api/auth/',
        include('accounts.urls')
    ),

    path(
        'api/auth/login/',
        CustomTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    path(
        'api/auth/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    path(
        'api/patients/',
        include('patients.urls')
    ),

    path(
        'api/treatments/',
        include('treatments.urls')
    ),

    path(
        'api/appointments/',
        include('appointments.urls')
   ),

   path(
        'api/appointments/',
        include('appointments.urls')
   ),
]