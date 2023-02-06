from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import token_obtain_pair, token_refresh




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('app1.urls')),
    path('registe/', include('auth_app.urls')),
    path('accesstoken/', token_obtain_pair),
    path('refresh_token/', token_refresh),
    
    
]
