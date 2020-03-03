from django.shortcuts import render, redirect
from django.views.generic import (TemplateView,CreateView,ListView,DeleteView,CreateView,
                                  DetailView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MediaVideoModel,MediaImageModel,MediaAudioModel
from .forms import MediaVideoForm,MediaImageForm,MediaAudioForm
# Create your views here.

class ActivitiesView(TemplateView):
    template_name = 'resources/homework_home.html'

class DownloadsView(TemplateView):
    template_name = 'resources/library_home.html'

class GamesView(TemplateView):
    template_name = 'resources/games_home.html'

class GlossaryView(TemplateView):
    template_name = 'resources/glossary_home.html'


############################################################################################
####                                   DISPLAY VIEW                                    ####
############################################################################################

def display_media(request):
    videos = MediaVideoModel.objects.all()
    images = MediaImageModel.objects.all()
    audio = MediaAudioModel.objects.all()
    context = {'videos': videos,
                'images': images,
                'audio': audio
                }
    template_name ='resources/media_home.html'
    return render (request, 'resources/media_home.html', context)

############################################################################################
####                                   MEDIA VIDEO                                      ####
############################################################################################

class UploadVideoView(LoginRequiredMixin,CreateView):
    template_name = 'resources/media/media_video_upload_form.html'
    login_url = '/accounts/login/'
    success_url = reverse_lazy('resources:media')
    form_class = MediaVideoForm
    model = MediaVideoModel

class VideoDetailView(DetailView):
    template_name = 'resources/media/media_video_detail.html'
    model = MediaVideoModel

class VideoDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'resources/media/media_video_delete_form.html'
    model = MediaVideoModel
    success_url = reverse_lazy('resources:media')



############################################################################################
####                                   MEDIA IMAGE                                      ####
############################################################################################

def image_upload(request):
    if request.method == 'POST':
        form = MediaImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resources:media')
    else:
        form = MediaImageForm()
    return render(request, 'resources/media/media_image_upload_form.html', {
        'form': form
    })

class ImageDetailView(DetailView):
    template_name = 'resources/media/media_image_detail.html'
    model = MediaImageModel

class ImageDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'resources/media/media_image_delete_form.html'
    model = MediaImageModel
    success_url = reverse_lazy('resources:media')

############################################################################################
####                                   MEDIA AUDIO                                      ####
############################################################################################

def audio_upload(request):
    if request.method == 'POST':
        form = MediaAudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resources:media')
    else:
        form = MediaAudioForm()
    return render(request, 'resources/media/media_audio_upload_form.html', {
        'form': form
    })

class AudioDetailView(DetailView):
    template_name = 'resources/media/media_audio_detail.html'
    model = MediaAudioModel

class AudioDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'resources/media/media_audio_delete_form.html'
    model = MediaAudioModel
    success_url = reverse_lazy('resources:media')
