from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('api/',views.api_view),
]