from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.InputView.as_view(), name='input'),
]
