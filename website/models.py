from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    Uploaded_at = models.DateTimeField(auto_now_add=True)
    fileName = models.CharField(max_length=300)