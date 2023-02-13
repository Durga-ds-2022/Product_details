from django.urls import path
from home.views import *

urlpatterns = [
       path('', home, name= 'home'),
       path('create-order/', create, name= 'create-order'),
    #    path('edit/<int:id>/', edit, name= "edit"),
       path('update/<int:id>', update, name= "update"),
       path('delete/<int:id>/', del_product, name= "del_product"),


]