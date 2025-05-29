from django.urls import path
from . import views

app_name = "Main"

urlpatterns = [
    path('', views.index, name='index'),
    path('error-404/', views.error_404_demo, name='error_404_demo')
]