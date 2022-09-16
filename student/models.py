from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    regno=models.CharField(max_length=6, unique=True)
    # department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name