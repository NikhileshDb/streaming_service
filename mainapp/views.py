from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . models import EncodedFiles, StoreFile, DataEncoder_Settings
from .form import FileUploadForm
from streamer.controller_node import ControllerNode
from streamer.node_base import ProcessStatus

import os
from mystreamer.settings import BASE_DIR


from media.encoder.encoder import encode


def home(request):
    return render(request, 'home.html')

# Raw Video Uploader
def upload_video(request):
    form = FileUploadForm()
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'upload_video.html', {'form': form})


# Render video objects for endoding settings
def initialize_video_encoding(request):
    
    obj_settings = DataEncoder_Settings.objects.all()
    context ={
        
        'obj_settings': obj_settings
    }
    return render(request, 'configuration.html', context)


# Save the configurations for encoding
def handle_configuration(request):
    if request.method == 'POST':
        media_obj_id = request.POST.get('videos')
        item = StoreFile.objects.get(id=media_obj_id)
        media_file_path = item.mediaFile.path
        setting_name =  request.POST.get('setting_name')
        output_folder = request.POST.get('output_folder')
        file_path = "media/{}".format(output_folder)
        try:
            xpath = os.mkdir(file_path)
            print(file_path)
            data = DataEncoder_Settings.objects.create(
                name = setting_name,
                output_location = file_path, 
                File_Url = media_file_path, 
                media_type= 'video', 
                segment_folder = 'segments',
                dash_output = f'{file_path}/dash.mpd', 
                hls_output = f'{file_path}/hls.m3u8'
            )
            data.save()
        except:
                HttpResponse("Error")
    return HttpResponse("Sucess")


hlspath = os.path.join(BASE_DIR, 'media/hls')
   
mhlspath = os.path.abspath(hlspath)


# ENCODER FUNCTION
controller = ControllerNode()
def encode_the_video(pk):
    obj = DataEncoder_Settings.objects.get(id=pk)
    controller.start(
        output_location= obj.output_location,
        input_config_dict= {
            'inputs': [
                dict(name=obj.File_Url, media_type=obj.media_type),
                dict(name=obj.File_Url, media_type='audio'),
            ]
            },
         pipeline_config_dict= {
            'streaming_mode': 'vod',
            'resolutions': ['1080p', '720p', '480p'],
            'channel_layouts': ['stereo'],
            'video_codecs': ['h264'],
            'audio_codecs': ['aac'] ,
            'manifest_format': ['hls', 'dash'],
            'segment_size': 10,
            'segment_per_file': True,
            
        },
        use_hermetic= True,
    )



# Enconding handler call the encoder function
def start_encoding(request):
    if request.method == 'POST':
        obj  = request.POST.get('settings')
        try:
            encode_the_video(obj)
            return HttpResponse('Encoding Started')
        except:
            return HttpResponse('Something Went wrong')



def testing_view(request):
    obj = StoreFile.objects.all()
    obj_settings = DataEncoder_Settings.objects.all()
    context ={
        'obj': obj,
        'obj_settings': obj_settings
    }
    return render(request, 'encoding_setting.html', context)