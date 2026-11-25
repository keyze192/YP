from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('my-login/',LoginView.as_view(success_url=reverse_lazy('main')),name='login'),
    path('request/', views.create_request, name='request'),
]