from rest_framework import serializers
from .models import Producer, ProducerTransaction

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = (
                'producerId',
                'first_name',
                'last_name',
                'address',
                'email',
                'phone_number',
                'payment_method',
                'box_premium',
                'box_common',
                )
        
class ProducerTransactionSerializer(serializers.ModelSerializer):
    producer_name = serializers.CharField(source='producer.get_producer_full_name', read_only=True)
    class Meta:
        model = ProducerTransaction
        fields = (
                'producerTransactionId',
                'producer',
                'producer_name',
                'date',
                'transaction_type',
                'box_type',
                'box_qtt',
                'price',
                )

