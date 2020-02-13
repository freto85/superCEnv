from django.shortcuts import render
from django.views.generic import TemplateView

class BadgesView(TemplateView):
    template_name = 'badges/badges_home.html'
