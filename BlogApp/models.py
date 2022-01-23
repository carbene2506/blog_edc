from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=1000)
    username = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']