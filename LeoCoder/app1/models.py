from django.db import models


# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)

class Appointment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
