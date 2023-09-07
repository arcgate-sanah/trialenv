from django.db import models

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
