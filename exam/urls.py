
from django.urls import path
from . import views

urlpatterns = [
    path('test/' ,views.test),
    path('result/',views.result),
]
