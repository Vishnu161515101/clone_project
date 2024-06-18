from django.urls import path,include
from . import views

urlpatterns = [

   path('',views.vishnu,name='vishnu'),
   path('home',views.home,name='home'),
   path('image_test1',views.image_test1,name='image_test1'),
   path('vishnu12',views.vishnu12,name='vishnu12'),
   path('popup',views.popup,name='popup'),

]
