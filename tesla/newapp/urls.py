from django.conf.urls.static import static
from django.urls import path, include

from newapp import views, admin
from tesla import settings

urlpatterns = [
   path('', views.demo, name="demo"),

]
