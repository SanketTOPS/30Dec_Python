from django.db import models

# Create your models here.

class userinfo(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    mobile=models.BigIntegerField()
    address=models.TextField()
