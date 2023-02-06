from django.urls import path
from .views import MobileAPIView, MobileDetailGenericView


urlpatterns = [
    path('post/',MobileAPIView.as_view()),
    path('blog/<int:pk>/', MobileDetailgenricView.as_view())
]