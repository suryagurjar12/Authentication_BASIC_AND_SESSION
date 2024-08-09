from django.db import models

# Create your models here.
class SchoolModel(models.Model):
    stu_name=models.CharField(max_length=50)
    Stu_email=models.EmailField()
    stu_roll=models.IntegerField()
    def __str__(self):
        return self.stu_name
