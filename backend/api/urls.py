from django.urls import path

from api import views

# from .views import api_home


urlpatterns = [
    path('', views.api_home) # localhost:8000/api/

]