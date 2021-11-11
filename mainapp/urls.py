from django.urls import path
from . views import home, upload_video


urlpatterns =[
    path('', home),
    path('upload/', upload_video, name='upload_video'),
]