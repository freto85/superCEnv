from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class RewardsView(TemplateView):
    template_name = 'rewards/rewards_home.html'

class RoadmapView(TemplateView):
    template_name = 'rewards/roadmap.html'
