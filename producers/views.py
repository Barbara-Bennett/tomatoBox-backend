from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Producer, ProducerTransaction
from .serializers import ProducerSerializer, ProducerTransactionSerializer

class ProducerView(APIView):

    def post(self, request):
        data = request.data 
        serializer = ProducerSerializer(data=data)  

        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse("Producer Added Successfully", safe=False)
        return JsonResponse("Failed to Add Producer", safe=False)
    def get_producer(self, pk):
        try:
            producer = Producer.objects.get(producerId=pk)
            return producer
        except Producer.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_producer(pk)
            serializer = ProducerSerializer(data)
        else:
            data = Producer.objects.all()
            serializer = ProducerSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None):
        producer_to_update = Producer.objects.get(producerId=pk)
        serializer = ProducerSerializer(instance=producer_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Producer updated Successfully", safe=False)
        return JsonResponse("Failed To Update Producer")


    def delete(self, request, pk):
        producer_to_delete = Producer.objects.get(producerId=pk)
        producer_to_delete.delete()
        return JsonResponse("Producer Deleted Successfully", safe=False)
    

class ProducerTransactionView(APIView):

    def post(self, request):
        data = request.data 
        serializer = ProducerTransactionSerializer(data=data) 

        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse("Transaction Added Successfully", safe=False)
        return JsonResponse("Failed to Add Transaction", safe=False)

    def get_producer_transaction(self, pk):
        try:
            producer_transactions = ProducerTransaction.objects.get(producerTransactionId=pk)
            return producer_transactions
        except ProducerTransaction.DoesNotExist:
            raise Http404


    def get(self, request, pk=None):
        if pk:
            transaction = self.get_producer_transaction(pk)
            serializer = ProducerTransactionSerializer(transaction)
            return Response(serializer.data)  # Return serialized data
        else:
            transactions = ProducerTransaction.objects.all()
            serialized_transactions = []
            for transaction in transactions:
                transaction_data = ProducerTransactionSerializer(transaction).data
                producer_id = transaction.producer_id  
                producer_full_name = self.get_producer_full_name(producer_id)
                transaction_data['producer_name'] = producer_full_name
                serialized_transactions.append(transaction_data)

            return Response(serialized_transactions)

    def put(self, request, pk=None):
        producer_transaction_to_update = ProducerTransaction.objects.get(producerTransactionId=pk)
        serializer = ProducerTransactionSerializer(instance=producer_transaction_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Transaction updated Successfully", safe=False)
        return JsonResponse("Failed To Update Transaction")


    def delete(self, request, pk):
        producer_transaction_to_delete = ProducerTransaction.objects.get(producerTransactionId=pk)
        producer_transaction_to_delete.delete()
        return JsonResponse("Transaction Deleted Successfully", safe=False)
    
    def get_producer_full_name(self, producer_id):
        try:
            producer = Producer.objects.get(producerId=producer_id)
            return producer.get_producer_full_name()
        except Producer.DoesNotExist:
            return f"Unknown Producer (ID: {producer_id})"