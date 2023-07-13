from django.db import models

# Create your models here.
class Students(models.Model):
    std_name = models.CharField(max_length=50)
    std_id = models.IntegerField()
    std_course = models.CharField(max_length=50)
    std_Phone_no = models.CharField(max_length=50)
    std_class = models.CharField(max_length=20)

