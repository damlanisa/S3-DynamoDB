from django.db import models


class Upload(models.Model):
    file = models.FileField(upload_to='uploaded_files', max_length=500)
    table_name = models.CharField(max_length=100) 
    upload_time = models.DateTimeField(auto_now_add=True)
