from django.urls import path
from listings import views


urlpatterns = [
    path('', views.indexl),

]
