from django.urls import path
from . views import home, upload_video, initialize_video_encoding, handle_configuration, start_encoding, testing_view


urlpatterns =[
    path('', home),
    path('upload/', upload_video, name='upload_video'),
    path('encoding/', initialize_video_encoding, name='configuration'),
    path('handle/', handle_configuration, name='handle'),
    path('start_encoding', start_encoding, name='start_encoding'),
    path('setting/', testing_view, name='testing'),
]