from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('my-login/', LoginView.as_view(success_url=reverse_lazy('main')), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('request/', views.create_request, name='request'),
    path('services/', views.services_list, name='services'),
    path('accounts/profile/', views.profile_view, name='profile'),
]