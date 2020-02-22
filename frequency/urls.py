from django.urls import path
from frequency import views
urlpatterns = [
    path('', views.home),
]
