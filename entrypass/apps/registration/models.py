from django.db import models

# Create your models here.
class Registration(models.Model):
    rollno = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    status = models.CharField(max_length=50, default='Pending')
    unique_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



    