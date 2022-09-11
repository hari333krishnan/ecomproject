from django.urls import path
from accounts import views


urlpatterns = [
    path('registration/',views.register,name='registration'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]