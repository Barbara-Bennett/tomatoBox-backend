from rest_framework import serializers
from .models import Merchant, MerchantTransaction

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = (
                'merchantId',
                'first_name',
                'last_name',
                'address',
                'email',
                'phone_number',
                'payment_method',
                'box_premium',
                'box_common',
                )
        
class MerchantTransactionSerializer(serializers.ModelSerializer):
    merchant_name = serializers.CharField(source='merchant.get_merchant_full_name', read_only=True)
    class Meta:
        model = MerchantTransaction
        fields = (
                'merchantTransactionId',
                'merchant',
                'merchant_name',
                'date',
                'transaction_type',
                'box_type',
                'box_qtt',
                'price',
                )

