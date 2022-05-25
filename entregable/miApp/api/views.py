from django.views.generic import View
from rest_framework.views import APIView
from miApp.models import entryModel
from miApp.api.serializers import EntrySerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class EntryListAPI(APIView):
    def get(self, request):
        
        #engancha la vista con el modelo de datos
        entries = entryModel.objects.all()
        
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data)
    
        
    def post(self, request):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
class EntryDetailAPI(APIView):
    def get_entry(self, request, pk):
        entries = get_object_or_404(entryModel, pk=pk)
        #self.check_object_permissions(request, entries)
        return entries
    
    def get(self, request, pk):

        entries = self.get_entry(request, pk)

        serializer = EntrySerializer(instance=entries)
        return Response(serializer.data)
    
    def put(self, request, pk):

        #user = User.object.get(pk=pk)
        entries = get_object_or_404(entryModel, pk=pk)

        #self.check_object_permissions(request, entries)

        serializer = EntrySerializer(instance=entries, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    
    def delete(self, request, pk):
        #self.check_permissions(request)

        entries = get_object_or_404(entryModel, pk=pk)

        #self.check_object_permissions(request, user)

        entries.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)