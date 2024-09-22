from django.db import models

# Create your models here.
class Login_Data(models.Model):
  e_mail = models.EmailField()
  password = models.CharField(max_length=8)