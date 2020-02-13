from django.urls import path
from . import views

urlpatterns = [
    path('rewards/',views.RewardsView.as_view(),name='rewards'),
    path('roadmap/',views.RoadmapView.as_view(),name='roadmap'),
]
