from django.contrib import admin
from .models import StoreFile, DataEncoder_Settings, EncodedFiles



admin.site.register(StoreFile)
admin.site.register(DataEncoder_Settings)
admin.site.register(EncodedFiles)
