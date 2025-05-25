from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    medical_history = models.TextField()