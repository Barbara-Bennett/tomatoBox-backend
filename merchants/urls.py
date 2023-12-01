from django.urls import path
from .views import MerchantView, MerchantTransactionView

urlpatterns = [
    path('merchants/', MerchantView.as_view()),
    path('merchants/<int:pk>/', MerchantView.as_view()),
    path('merchants-transactions/', MerchantTransactionView.as_view()),
    path('merchants-transactions/<int:pk>/', MerchantTransactionView.as_view()),
]