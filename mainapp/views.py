from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . models import StoreFile
from .form import FileUploadForm

def home(request):
    return render(request, 'home.html')


def upload_video(request):
    form = FileUploadForm()
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'upload_video.html', {'form': form})



