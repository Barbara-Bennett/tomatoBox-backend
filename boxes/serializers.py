from rest_framework import serializers
from .models import Box


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = (
                'box_type',
                'new_boxes',
                'qtt_total',
                'box_qtt',
                'damaged_box_qtt',
                'borrowed_producer',
                'borrowed_merchant',
            ) 