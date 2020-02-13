from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

class SpecialPage(TemplateView):
    template_name = 'special/special_home.html'

# Create your views here.
