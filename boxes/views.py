# Create your views here.
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Box
from .serializers import BoxSerializer


class BoxView(APIView):

    def post(self, request):
        data = request.data
        serializer = BoxSerializer(data=data)  

        if serializer.is_valid(): 
            serializer.save()
            return JsonResponse("Box Added Successfully", safe=False)
        return JsonResponse("Failed to Add Box", safe=False)

    def get_box(self, pk):
        try:
            box = Box.objects.get(box_type=pk)
            return box
        except Box.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_box(pk)
            serializer = BoxSerializer(data)
        else:
            data = Box.objects.all()
            serializer = BoxSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None):
        box_to_update = Box.objects.get(box_type=pk)
        serializer = BoxSerializer(instance=box_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Box updated Successfully", safe=False)
        return JsonResponse("Failed To Update Box")

    def delete(self, request, pk):
        box_to_delete = Box.objects.get(box_type=pk)
        box_to_delete.delete()
        return JsonResponse("Box Deleted Successfully", safe=False)
    

