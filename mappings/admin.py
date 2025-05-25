from django.contrib import admin
from .models import Mapping

@admin.register(Mapping)
class MappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'doctor_name')

    def patient_name(self, obj):
        return obj.patient.name
    patient_name.admin_order_field = 'patient'  # Allows column order sorting
    patient_name.short_description = 'Patient Name'

    def doctor_name(self, obj):
        return obj.doctor.name
    doctor_name.admin_order_field = 'doctor'
    doctor_name.short_description = 'Doctor Name'
