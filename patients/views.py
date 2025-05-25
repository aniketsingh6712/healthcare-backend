from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Patient
from .serializers import PatientSerializer
from django.shortcuts import get_object_or_404

class PatientListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        patients = Patient.objects.filter(user=request.user)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        return get_object_or_404(Patient, pk=pk, user=user)

    def get(self, request, pk):
        patient = self.get_object(pk, request.user)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        patient = self.get_object(pk, request.user)
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        patient = self.get_object(pk, request.user)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


