from . models import StoreFile
from django.forms import  ModelForm


class FileUploadForm(ModelForm):
    class Meta:
        model = StoreFile
        fields = '__all__'