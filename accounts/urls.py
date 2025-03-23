from django.urls import path
from .views import MyCustomLogin
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', MyCustomLogin.as_view(
        template_name='accounts/login.html'), name='user-login'),
        path('logout/', auth_views.LogoutView.as_view(
        template_name='accounts/logout.html'), name='user-logout')
]