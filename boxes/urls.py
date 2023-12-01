from django.urls import path
from .views import BoxView

urlpatterns = [
    path('boxes/', BoxView.as_view()),
    path('boxes/<pk>/', BoxView.as_view()),
    ]