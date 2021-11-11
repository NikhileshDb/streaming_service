from django.db import models
from django.db.models.enums import Choices

# Create your models here.
from streamer.controller_node import ControllerNode


# GUI to upload Video and Audio file
class StoreFile(models.Model):
    file_name = models.CharField(max_length=75)
    mediaFile = models.FileField(upload_to='media/')

    def __str__(self):
        return self.file_name