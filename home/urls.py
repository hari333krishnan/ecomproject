
from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:c_slug>/',views.home, name='home_cat'),
    path('<slug:c_slug>/<slug:prod_slug>',views.ProdDetails, name='details'),
    path('searching',views.Searching, name='searching')

]