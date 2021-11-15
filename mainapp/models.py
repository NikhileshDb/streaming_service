from django.db import models
from django.db.models.enums import Choices

# Create your models here.
from streamer.controller_node import ControllerNode


# GUI to upload Video and Audio file
class StoreFile(models.Model):
    file_name = models.CharField(max_length=75)
    mediaFile = models.FileField(upload_to='')
    file_url = models.URLField(blank=True)

    def __str__(self):
        return self.file_name


class DataEncoder_Settings(models.Model):
    name = models.CharField(max_length=50, blank=True)
    output_location = models.CharField(max_length=50, null=True)
    File_Url = models.URLField(blank=True,  null=True)
    media_type = models.CharField(max_length=10,  null=True)
    segment_folder = models.CharField(max_length=50,  null=True)
    dash_output = models.URLField(blank=True)
    hls_output = models.URLField(blank=True)

    def __str__(self):
        return self.name

class EncodedFiles(models.Model):
    dash_output_url = models.URLField(blank=True)
    hls_output_url = models.URLField(blank=True)
