from django.shortcuts import render,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (TemplateView,ListView)

from .models import Document, Audio
from .forms import DocumentForm, AudioForm

class StationView(ListView):
    model = Document
    template_name = 'station/station_home.html'



class StationAudioView(ListView):
    model = Audio
    template_name = 'station/station_audio.html'

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('station:station_home')
    else:
        form = DocumentForm()
    return render(request, 'station/model_form_upload.html', {
        'form': form
    })

def model_form_audio_upload(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('station:station_audio_home')
    else:
        form = AudioForm()
    return render(request, 'station/model_audio_form_upload.html', {
        'form': form
    })
