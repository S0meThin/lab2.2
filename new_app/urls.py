from django.urls import path
from new_app import views

urlpatterns = [
    path('', views.PageView.as_view()),
]