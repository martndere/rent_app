from django.db import models
from django.conf import settings

# Create your models here.
class Verification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_document = models.FileField(upload_to='ids/')
    is_verified = models.BooleanField(default=False)
    submitted_on = models.DateTimeField(auto_now_add=True)
