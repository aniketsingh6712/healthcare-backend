from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'user', 'name', 'age', 'medical_history']
