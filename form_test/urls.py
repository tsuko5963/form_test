from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.InputView.as_view(), name='input'),
    path('input2/', views.Input2View.as_view(), name='input2'),
    path('confirm/', views.ConfirmView.as_view(), name='confirm'),
    path('thankyou/', views.ThankyouView.as_view(), name='thankyou'),
]
