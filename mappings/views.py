from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Mapping
from .serializers import MappingSerializer

class MappingListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        mappings = Mapping.objects.all()
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MappingDetailPatientView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        # Interpret id as patient_id and get all mappings for that patient
        mappings = Mapping.objects.filter(patient__id=id)
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        # Interpret id as mapping id and delete that mapping
        mapping = get_object_or_404(Mapping, pk=id)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
