from django.urls import path
from .views import ProducerView, ProducerTransactionView

urlpatterns = [
    path('producers/', ProducerView.as_view()),
    path('producers/<int:pk>/', ProducerView.as_view()),
    path('producers-transactions/', ProducerTransactionView.as_view()),
    path('producers-transactions/<int:pk>/', ProducerTransactionView.as_view()),
    ]
