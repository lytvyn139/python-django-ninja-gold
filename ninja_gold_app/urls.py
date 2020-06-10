from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reset_all', views.reset_all),
    path('reset_scores', views.reset_scores),
    path('process_money', views.process)
]