from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Merchant, MerchantTransaction
from .serializers import MerchantSerializer, MerchantTransactionSerializer

class MerchantView(APIView):

    def post(self, request):
        data = request.data
        serializer = MerchantSerializer(data=data)

        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse("Merchant Added Successfully", safe=False)
        return JsonResponse("Failed to Add Merchant", safe=False)

    def get_merchant(self, pk):
        try:
            merchant = Merchant.objects.get(merchantId=pk)
            return merchant
        except Merchant.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_merchant(pk)
            serializer = MerchantSerializer(data)
        else:
            data = Merchant.objects.all()
            serializer = MerchantSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None):
        merchant_to_update = Merchant.objects.get(merchantId=pk)
        serializer = MerchantSerializer(instance=merchant_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Merchant updated Successfully", safe=False)
        return JsonResponse("Failed To Update Merchant")

    def put(self, request, pk=None):
        merchant_to_update = Merchant.objects.get(merchantId=pk)
        serializer = MerchantSerializer(instance=merchant_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Merchant updated Successfully", safe=False)
        return JsonResponse("Failed To Update Merchant")


    def delete(self, request, pk):
        merchant_to_delete = Merchant.objects.get(merchantId=pk)
        merchant_to_delete.delete()
        return JsonResponse("Merchant Deleted Successfully", safe=False)
    

class MerchantTransactionView(APIView):

    def post(self, request):
        data = request.data 
        serializer = MerchantTransactionSerializer(data=data)  

        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse("Transaction Added Successfully", safe=False)
        return JsonResponse("Failed to Add Transaction", safe=False)

    def get_merchant_transaction(self, pk):
        try:
            merchant_transactions = MerchantTransaction.objects.get(merchantTransactionId=pk)
            return merchant_transactions
        except MerchantTransaction.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            transaction = self.get_merchant_transaction(pk)
            serializer = MerchantTransactionSerializer(transaction)
            return Response(serializer.data)  
        else:
            transactions = MerchantTransaction.objects.all()
            serialized_transactions = []
            for transaction in transactions:
                transaction_data = MerchantTransactionSerializer(transaction).data
                merchant_id = transaction.merchant_id  
                merchant_full_name = self.get_merchant_full_name(merchant_id)
                transaction_data['merchant_name'] = merchant_full_name
                serialized_transactions.append(transaction_data)

            return Response(serialized_transactions)  


    def put(self, request, pk=None):
        merchant_transaction_to_update = MerchantTransaction.objects.get(merchantTransactionId=pk)
        serializer = MerchantTransactionSerializer(instance=merchant_transaction_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Transaction updated Successfully", safe=False)
        return JsonResponse("Failed To Update Transaction")


    def delete(self, request, pk):
        merchant_transaction_to_delete = MerchantTransaction.objects.get(merchantTransactionId=pk)
        merchant_transaction_to_delete.delete()
        return JsonResponse("Transaction Deleted Successfully", safe=False)
    
    def get_merchant_full_name(self, merchant_id):
        try:
            merchant = Merchant.objects.get(merchantId=merchant_id)
            return merchant.get_merchant_full_name()
        except Merchant.DoesNotExist:
            return f"Unknown Merchant (ID: {merchant_id})"