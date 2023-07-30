from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.InputView.as_view(), name='input'),
    path('input2/', views.Input2View.as_view(), name='input2'),
    path('confirm/', views.ConfirmView.as_view(), name='confirm'),
    path('thankyou/', views.ThankyouView.as_view(), name='thankyou'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
]
