from django.db import models
from apps.registration.models import Registration
# Create your models here.

class EntryPass(models.Model):
    name = models.OneToOneField(Registration, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=50)
    qr_code = models.ImageField(upload_to='qr_codes/')
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    unique_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
