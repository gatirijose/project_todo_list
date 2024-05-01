from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', UserCreateView.as_view(),name='sign-up'),
    path('project/<int:proj_num>/', project_details,name='proj_details'),
]
