from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path,include
from .views import register
#import social_django

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('registration/',register,name='register'),
    path('logout',LogoutView.as_view(),name='logout'),

]